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
Participants(_, id, _, ptype, %s, _):-
Actor( id, ptype, _, aliasList ),
contains( aliasList, %s )
""" %(some_name, some_name)


query1 = """
Participants(_, id, _, ptype, %s, _):-
Aliases( sid, aliasList ),
AgentType( sid, ptype ),
CONTAINS( aliasList, %s )
""" %(some_name, some_name)

query2 = """
Participants(_, id_to_sid(sid), _, %s, pname, _):-
Actor( sid, %s, pname, _ )
""" %(group, group)


query3 = """
Participants(_, id, _, %s, pname, _):-
AgentType( id, group),
AgentName( id, pname )
""" %group

query4 = """
Participants(_, %s, _, ptype, pname, _):-
Actor( sid_to_id(%s), _, pname, _ ),
Type( sid_to_id(%s), ptype )
""" % (some_id, some_id, some_id)


query5 = """
ParticipantDetails(_, _, org, country, %s, _):-
From( id, country ),
Affiliation( id, org, _, _ ),
Actor( id, _, _, aliasList )
"""

query6 = """
ParticipantDetails(_, _, org, country, %s, _):-
From( id, country ),
Affiliation( id, org, _, _ ),
Actor( id, _, _, aliasList )
"""

query7 = """
ParticipantDetails(_, _, category, _, 'Some Name', _):-
AgentName(id, pname),
AgentType(id, ptype),
Aliases( id, aliasList )
"""

query8 = """
ParticipantDetails(_, _, category, _, 'Some Name', _):-
AgentName(id, pname),
AgentType(id, ptype),
Aliases( id, aliasList ),
AgentSector( id, sector_id ),
SectorName( sector_id, sector_name1 )"""

datalog_queries = [query0, query1, query2, query3, query4, query5, query6, query7, query8]
