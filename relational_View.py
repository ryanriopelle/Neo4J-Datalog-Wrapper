from datalog import *
from datalogTestQueries import *
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


#Print datatypes
print "Actor:", "\n", Actor.dtypes,"\n"
print "From:", "\n", From.dtypes,"\n"
print "Affiliation:", "\n", Affiliation.dtypes,"\n"
print "AgentName:", "\n", AgentName.dtypes,"\n"
print "AgentType:", "\n", AgentType.dtypes,"\n"
print "Aliases:", "\n", Aliases.dtypes,"\n"
print "AgentSector:", "\n", AgentSector.dtypes,"\n"
print "SectorName:", "\n", SectorName.dtypes,"\n"
print "SectorIs_A:", "\n", SectorIs_A.dtypes




