

# from neo4j.v1 import GraphDatabase, basic_auth
# driver = GraphDatabase.driver("bolt://54.85.112.231:7687", auth=basic_auth("neo4j", "LEbKqX3q"))
# session = driver.session()
#
# result = session.run("Match (n:Country)-[a]-(b) Return distinct n")
# for record in result:
#     print record
# session.close()




from py2neo import authenticate, Graph
from pandas import DataFrame

#Sets up connection to Neo4J
authenticate("54.85.112.231:7474", "neo4j", "LEbKqX3q")
graph = Graph("bolt://54.85.112.231/db/data/")


#Relational Tables For Schema A
Actor = DataFrame(graph.data("Match (a:Actor) Return distinct ID(a) as id, a.Type as ptype, a.Name as pname, a.AliasList as AliasList"))
From = DataFrame(graph.data("MATCH (a:Actor)-[:From]-(c:Country) RETURN ID(a) as id,c.Name as country"))
Affiliation = DataFrame(graph.data("MATCH (a:Actor)-[r:Affiliation]-(o:Organization) RETURN ID(a) as id,o.Name as org, r.beginDate as start, r.endDate as end"))

#Relational Tables For Schema B

AgentName = DataFrame(graph.data("Match (a:AgentName) Return ID(a) as id, a.Name as pname"))
AgentType = DataFrame(graph.data("Match (a_n:AgentName)-[:AgentType]-(a_t:AgentType) Return ID(a_n) as id, a_t.Name as ptype"))
Aliases = DataFrame(graph.data("Match (a_n:AgentName)-[:AgentAlias]-(a:Aliases) Return ID(a_n) as id, a.AliasList as alias"))
AgentSector = DataFrame(graph.data("Match (a:AgentName)-[:Sector]-(s:Sector) Return ID(a) as id, ID(s) as sector_id"))
SectorName = DataFrame(graph.data("Match (s:Sector) Return ID(s) as sector_id, s.Name as name"))
SectorIs_A = DataFrame(graph.data("MATCH p=(s1:Sector)-[:`is-a`]->(s2:Sector) RETURN ID(s1) as sector_id, ID(s2) as sector_id2 LIMIT 25"))


#Send all dataframes to a compressed HDF store in memory
Actor.to_hdf( "Neo4JRelational.hdf", "Actor", complib='blosc')
From.to_hdf( "Neo4JRelational.hdf", "From", complib='blosc')
Affiliation.to_hdf( "Neo4JRelational.hdf", "Affiliation", complib='blosc')
AgentName.to_hdf( "Neo4JRelational.hdf", "AgentName", complib='blosc')
AgentType.to_hdf( "Neo4JRelational.hdf", "AgentType", complib='blosc')
Aliases.to_hdf( "Neo4JRelational.hdf", "Aliases", complib='blosc')
AgentSector.to_hdf( "Neo4JRelational.hdf", "AgentSector", complib='blosc')
SectorName.to_hdf( "Neo4JRelational.hdf", "SectorName", complib='blosc')
SectorIs_A.to_hdf( "Neo4JRelational.hdf", "SectorIs_A", complib='blosc')