from neo4j.v1 import GraphDatabase, basic_auth


# driver = GraphDatabase.driver("bolt://54.85.112.231:7687", auth=basic_auth("neo4j", "LEbKqX3q"))
# session = driver.session()
#
# result = session.run("Match (a:Actor) Return distinct a.Type, a.Name")
#
# type result
#
# for record in result:
#     print record, record[0], record[1]
# session.close()


#Py2Neo Makes It Easier Run Queries and Place Directly in Dataframe
from py2neo import authenticate, Graph
from pandas import DataFrame

# set up authentication parameters
authenticate("54.85.112.231:7473", "neo4j", "LEbKqX3q")

# connect to authenticated graph database
graph = Graph('https://54.85.112.231:7473/browser/')
print graph.dbms.database_name
print graph.dbms.keys()
print graph.match.im_class


rl_Participants_i3_i4 = DataFrame(graph.data("Match (a:Actor) Return distinct a.Type, a.Name"))
print rl_Participants_i3_i4
