from Datalog import *
from DatalogTestQueries import *
import py2neo
import pandas

#Read in data in to pandas dataframes
Actor = pandas.read_hdf("Neo4JRelational.hdf", "Actor")
From = pandas.read_hdf("Neo4JRelational.hdf", "From")
Affiliation = pandas.read_hdf("Neo4JRelational.hdf", "Affiliation")
AgentName = pandas.read_hdf("Neo4JRelational.hdf", "AgentName")
AgentType = pandas.read_hdf("Neo4JRelational.hdf", "AgentType")
Aliases = pandas.read_hdf("Neo4JRelational.hdf", "Aliases")
AgentSector = pandas.read_hdf("Neo4JRelational.hdf", "AgentSector")
SectorName = pandas.read_hdf("Neo4JRelational.hdf", "SectorName")
SectorIs_A = pandas.read_hdf("Neo4JRelational.hdf", "SectorIs_A")

#Print schema for relational database
print "Actor:", Actor.columns.values
print "From:", From.columns.values
print "Affiliation:", Affiliation.columns.values
print "AgentName:", AgentName.columns.values
print "AgentType:", AgentType.columns.values
print "Aliases:", Aliases.columns.values
print "AgentSector:", AgentSector.columns.values
print "SectorName:", SectorName.columns.values
print "SectorIs_A:", SectorIs_A.columns.values, "\n"


# for q in datalog_queries:
#     inspect(q)

#class JoinTables(query)
d = Datalog(datalog_queries[1])
print 'head:', d.head
print 'name:', d.name
print 'projection:', d.getList
print 'Join keys:', d.joinKeys
for x in d.relations:
    print x.name
    for a in x.attributes:
        print '\t', \
            x.attributes[a].name, \
            x.attributes[a].index, \
            x.attributes[a].isJoinPart

import pandas

def make_df(filename):
    df = pandas.DataFrame.from_csv(filename)
    name = filename.split('.')[0]
    df.columns = map(lambda col: '{}_{}'.format(str(col), name), df.columns)
    return df

filenames = !ls

dfs = [make_df(filename) for filename in filenames]

def join_dfs(ldf, rdf):
    return ldf.join(rdf, how='inner')

final_df = reduce(join_dfs, dfs) #that's the magic
final_df.head()