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

        # set attributes
        for a in attribs:
            # add attribute and it's index
            self.attributes[a] = DatalogAttribute(a,attribs.index(a))
            self.getList.append(a)

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


    def __init__(self, datalogQuery):

        self.relations = list()

        # get head and body of datalog query
        self.head, self.body = datalogQuery.split(':-', 2)

        # get name of query, it should be name of the projected relation and set datalog property
        super(Datalog, self).__init__(self.head.split('(')[0], datalogQuery)

        # set attributes and getlist properties for head/projection
        self.__parse__(self.datalog)

        # body should just be a list of relations and attributes
        px = '(\w+[(].+?[)])'
        for r in re.findall(px, self.body):
            # create relation object for each relation found in body
            self.relations.append(DatalogRelation(r))

        # find all join attributes in all relations
        a = [a for sub in self.relations for a in sub.attributes]

        # find common attributes and add to list of join keys
        self.joinKeys = list(set([x for x in a if a.count(x) > 1]))

        px = '(\w+[(].+?[)])'
        for s in self.relations:

            # get predicates from body
            p = [x.strip() for x in re.sub(px, '', self.body).split(',') if x.strip() <> '']

            # create predicate dictionary
            s.predicate = dict()
            s.predicateToList = list()

            if len(p) > 0:
                s.predicateToList = [x.strip() for x in re.sub(px, '', self.body).split(',') if x.strip() <> '']


                # only keep predicates for current relation
                s.predicateToList = [x for x in s.predicateToList if re.split('\W+',x)[0] in s.attributes]

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
    print '\n'

query = [
        # 'ans(L, A) :- group({X}, {Y}, p(X,Y,Z), L), count(L, A)',
        'Q(y):-test(x,y,z), blah(x,b,c)',
        #  "Q1(y, z):-test(x,y,z), blah(x,'some movie',c)",
         "Q2(y):-test(x, y, '20'), blah(x,'some movie',c), y > 10"
         ]

for q in query:
    inspect(q)