#This section provides a list of test queries that are used in the Neo4J to Parser File

#test variables that are input to string
org = 'Taliban'
group = 'Taliban'
some_name= 'some_name' #alias name
country = 'Taliban'
date = '2015-01-02'
date1= '2015-01-02'
date2 = '2015-01-02'
some_id ='some_id'


query0 = """
participants(_, id, _, ptype, %s, _):-
actor( id, ptype, _, aliaslist ),
contains( aliaslist, %s )
""" %(some_name, some_name)


query1 = """
participants(_, id, _, ptype, %s, _):-
aliases( sid, aliaslist ),
agenttype( sid, ptype ),
contains( aliaslist, %s )
""" %(some_name, some_name)

query2 = """
participants(_, id_to_sid(sid), _, %s, pname, _):-
actor( sid, %s, pname, _ )
""" %(group, group)


query3 = """
participants(_, id, _, %s, pname, _):-
agenttype( id, group),
agentname( id, pname )
""" %group

query4 = """
participants(_, %s, _, ptype, pname, _):-
actor( sid_to_id(%s), _, pname, _ ),
type( sid_to_id(%s), ptype )
""" % (some_id, some_id, some_id)


query5 = """
participantdetails(_, _, org, country, %s, _):-
from( id, country ),
affiliation( id, org, _, _ ),
actor( id, _, _, aliaslist )
"""

query6 = """
participantdetails(_, _, org, country, %s, _):-
from( id, country ),
affiliation( id, org, _, _ ),
actor( id, _, _, aliaslist )
"""

query7 = """
participantdetails(_, _, category, _, 'some name', _):-
agentname(id, pname),
agenttype(id, ptype),
aliases( id, aliaslist )
"""

query8 = """
participantdetails(_, _, category, _, 'some name', _):-
agentname(id, pname),
agenttype(id, ptype),
aliases( id, aliaslist ),
agentsector( id, sector_id ),
sectorname( sector_id, sector_name1 )"""

datalog_queries = [query0, query1, query2, query3, query4, query5, query6, query7, query8]
