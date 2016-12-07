import re
from argparse import _ActionsContainer


class DatalogBase(object):
    def __init__(self, name, datalog=None):
        self.name = name
        self.datalog = datalog
        self.attributes = dict()
        self.getList = list()

    def __parse__(self, query):
        # this method will create a list of attributes and getList property
        relations = re.findall('(\w+[(].+?[)])', query)

        r = relations[0]

        # this relies on the name of the class already being set
        attribs = [x.strip() for x in r[len(self.name)+1:-1].split(',')]

        for i in range(0, len(attribs)):
            # ignore columns that are not projected
            if attribs[i].strip() == '_' : continue

            self.attributes[attribs[i]] = DatalogAttribute(attribs[i], i)

            self.getList.append(attribs[i])

class DatalogAttribute(DatalogBase):

    def __init__(self, name, index):
        super(DatalogAttribute, self).__init__(name)
        self.isJoinPart = False
        self.index = index


class DatalogRelation(DatalogBase):

    def __init__(self, query):

        self.attributes = list()
        self.getList = list()
        self.predicate = None
        self.predicateToList = list()

        # set name & datalog property
        super(DatalogRelation, self).__init__(query.split('(')[0], query)

        # set attributes and getlist properties
        # super(DatalogRelation,self).__parse__(self.datalog)

        # get DatalogBase attributes
        self.__parse__(self.datalog)





class Datalog(DatalogBase):
    """Parse datalog query into it's components

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
    # group by columns
    gc = list()
    ag = list()


    def __init__(self, datalogQuery):

        self.relations = list()
        self.groupByColumns = list()
        self.aggregations = list()
        self.orderBy = None
        self.limit = None
        self.predicateToList = list()

        # get head and body of datalog query
        self.head, self.body = datalogQuery.split(':-', 2)

        # get name of query, it should be name of the projected relation and set datalog property
        super(Datalog, self).__init__(self.head.split('(')[0], datalogQuery)

        # set attributes and getlist properties for head/projection
        self.__parse__(self.datalog)

        # parse groupBy clause if it exists and return body without groupby clause
        remaining = self.__parse_groupBy__(self.body)

        # parse order by
        remaining = self.__parse_orderBy__(remaining)

        # parse limit
        remaining = self.__parse_limit__(remaining)

        # parse relations
        self.__parse_relations__(remaining)

    def __parse_limit__(self, body):
        #  this function extracts the limit clause

        px = '(LIMIT[(]\d+?[)])'

        o = [o.strip() for o in re.findall(px, body)]

        if len(o) > 0:
            body = body.replace(o[0], '')
            o = o[0]
            inner = o[o.find('(') + 1:-1]

            self.limit =  int(inner)

        return body

    def __parse_orderBy__(self, body):
        # extract order by clause
        px = '(SORT_BY[(].+?[)])'

        o = [o.strip() for o in re.findall(px, body)]

        if len(o) > 0:

            body = body.replace(o[0],'')
            o = o[0]
            inner = o[o.find('(') + 1:-1]

            parts = [x.strip() for x in inner.split(',')]
            self.orderBy = 'ORDER BY {0} {1}'.format(parts[0], parts[1][1:-1])

        return body

    def __parse_groupBy__(self, body):
        # parse and remove group by as it contains nested ()
        gx = '(GROUP_BY[(].+?[)][)])'
        self.groupBy = re.findall(gx, body)

        rel_pred = body
        # extract non-relational components
        for x in re.findall(gx, body):
            rel_pred = rel_pred.replace(x, '')

        # parse group by components
        for g in self.groupBy:
            # get inner contents of groupby()
            inner = g[g.find('(') + 1:-1]

            # get group by columns
            gc = re.findall('\[.+?\]', inner)[0]

            inner = inner.replace(gc, '').strip()

            # parse group columns into a list
            gc = [c.strip() for c in gc[1:-1].split(',')]

            # get aggregation variables
            ag = [a.strip() for a in inner.split(',') if a.strip() <> '']

            ag = ['{0} AS {1}'.format(a.split('=')[1].strip(), a.split('=')[0].strip()) for a in ag]

            self.groupByColumns = gc
            self.aggregations = ag

            pass
        return rel_pred



    def __parse_relations__(self, rel_pred):
        # body should just be a list of relations and predicates without any additional clauses
        px = '([a-z0-9]+[(].+?[)])'
        for r in re.findall(px, rel_pred):
            # create relation object for each relation found in body
            self.relations.append(DatalogRelation(r))
            # rel_pred = rel_pred.replace(r, '')

        # find all join attributes in all relations
        a = [a for sub in self.relations for a in sub.attributes]

        # find common attributes and add to list of join keys
        self.joinKeys = list(set([x for x in a if a.count(x) > 1]))

        # px = '(\w+[(].+?[)])'
        for s in self.relations:

            # get predicates from body
            p = [x.strip() for x in re.sub(px, '', rel_pred).split(',') if x.strip() <> '']

            # create predicate dictionary
            s.predicate = dict()
            s.predicateToList = list()


            if len(p) > 0:
                predicates = [x.strip() for x in p if x.strip() <> '']


                # only keep predicates for current relation
                s.predicateToList = [x for x in predicates if re.split('\W+',x)[0].strip() in s.attributes]



                # populate predicate dictionary
                for x in s.predicateToList:
                    s.predicate[s.attributes[re.split('\W+',x)[0]].index] = x

                #  check for inline equality predicates and add to predicate dictionary
                for x in s.attributes:
                    if x[0] == "'":
                        s.predicate[s.attributes[x].index] = x
                        s.predicateToList.append('{0} = {1}'.format(s.attributes[x].index, x.strip(u"'") if x.strip(u"'").isnumeric() else x))

            for x in set(self.joinKeys).intersection(s.getList):
                # use list of join keys to set join property to true
                s.attributes[x].isJoinPart = True

        if len(self.relations) > 1:
            attribs = reduce((lambda x, y: x.getList + y.getList),self.relations)
        else:
            attribs = self.relations[0].getList
        self.predicateToList = [x for x in predicates if not re.split('\W+', x)[0].strip() in attribs]
        pass



def inspect(query):
    # use to inspect object properties
    d = Datalog(query)
    print 'query:', query
    print 'head:',d.head
    print 'name:',d.name
    print 'projection:', d.getList

    print 'Join keys:',d.joinKeys
    for x in d.relations:
        print x.name
        print 'predicate:', x.predicateToList
        for a in x.attributes:
            print '\t', x.attributes[a].name, '\t', \
                x.attributes[a].index, '\t',\
                x.attributes[a].isJoinPart, '\t',\
                x.predicate[x.attributes[a].index] if x.attributes[a].index in x.predicate else ''
    print 'group by:', d.groupBy
    print 'grouping columns:', d.groupByColumns
    print 'aggregations:', d.aggregations
    print 'having clause:', d.predicateToList
    print 'order by:', d.orderBy
    # this property is an int
    print 'limit:', d.limit
print '\n'

# query = [
#         # 'ans(L, A) :- group({X}, {Y}, p(X,Y,Z), L), count(L, A)',
#         # 'Q(y):-test(x,y,_,_), blah(x,b, _)',
#         # 'A(a, b , d) :- rel(a, b, c, _), a > 1, GROUP_BY([a, b], d = COUNT(c)), d < 100, SORT_BY(b, "DESC"), f = FUN(d), LIMIT(25)'
#         #  "Q1(y, z):-test(x,y,z), blah(x,'some movie',c)",
#          "Q2(y):-test(x, y, '20'), blah(x,'some movie',c), y > 10"
#          ]

# for q in query:
#     inspect(q)