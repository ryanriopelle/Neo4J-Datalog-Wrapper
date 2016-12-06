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
print "Actor:", Actor.columns.values, "\n"\
"From:", From.columns.values, "\n" \
"Affiliation:", Affiliation.columns.values, "\n"\
"AgentName:", AgentName.columns.values, "\n" \
"AgentType:", AgentType.columns.values , "\n" \
"Aliases:", Aliases.columns.values , "\n" \
"AgentSector:", AgentSector.columns.values , "\n" \
"SectorName:", SectorName.columns.values , "\n" \
"SectorIs_A:", SectorIs_A.columns.values, "\n" \



print Actor.dtypes,"\n"
print From.dtypes,"\n"
print Affiliation.dtypes,"\n"
print AgentName.dtypes,"\n"
print AgentType.dtypes,"\n"
print Aliases.dtypes,"\n"
print AgentSector.dtypes,"\n"
print SectorName.dtypes,"\n"
print SectorIs_A.dtypes

# for q in datalog_queries:
#     inspect(q)

#class JoinTables(query)
# d = Datalog(datalog_queries[1])
# print 'head:', d.head
# print 'name:', d.name
# print 'projection:', d.getList
# print 'Join keys:', d.joinKeys
# for x in d.relations:
#     print x.name
#     for a in x.attributes:
#         print '\t', \
#             x.attributes[a].name, \
#             x.attributes[a].index, \
#             x.attributes[a].isJoinPart

