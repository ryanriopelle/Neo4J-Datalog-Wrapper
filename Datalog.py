import re

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

        # set name & datalog property
        super(DatalogRelation, self).__init__(query.split('(')[0], query)

        # set attributes and getlist properties
        # super(DatalogRelation,self).__parse__(self.datalog)

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
        for r in re.findall('(\w+[(].+?[)])', self.body):
            # create relation object for each relation found in body
            self.relations.append(DatalogRelation(r))

        # find all join attributes in all relations
        a = [a for sub in self.relations for a in sub.attributes]

        # find common attributes and add to list of join keys
        self.joinKeys = list(set([x for x in a if a.count(x) > 1]))

        for s in self.relations:
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
        for a in x.attributes:
            print '\t', x.attributes[a].name, x.attributes[a].index, x.attributes[a].isJoinPart
    print '\n'

query = ['Q(y):-test(x,y,z), blah(x,b,c)',
         "Q1(y, z):-test(x,y,z), blah(x,'some movie',c)",
         "Q2(y):-test(x, count{y}, z), blah(x,b,9)"]

for q in query:
    inspect(q)