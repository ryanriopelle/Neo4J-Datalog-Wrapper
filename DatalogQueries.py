
#This section provides a list of the queries presented in the neo4j schema mapping PDF

query1 = """MATCH (a:Actor) WHERE a.AliasList CONTAINS “Some Name” RETURN a.Type AS ptype, ID(a) AS sid"""
query2 = """MATCH (a:AgentName)-[:AgentAlias]->(n:Aliases), (a:AgentName)-[:AgentType]->(t:AgentType)
WHERE n.AliasList CONTAINS “Some Name” RETURN t.Name AS ptype, ID(a) AS sid"""
query3 = """MATCH (a:Actor)
WHERE a.Type = “Group”
return a.Name AS pname, ID(a) AS sid"""
query4 = """MATCH (a:AgentName)-[:AgentType]->(t:AgentType) WHERE t.Name = “Group”
RETURN a.Name AS pname, ID(a) AS sid"""
query5 = """MATCH (a:Actor)
WHERE ID(a) = 12345
RETURN a.Type AS ptype, a.Name AS pname"""
query6 = """MATCH (a:AgentName)-[:AgentType]->(t:AgentType) WHERE ID(a) = 12345
RETURN t.Name AS ptype, a.Name as pname"""
query7 = """
MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o:Organization)
WHERE a.AliasList CONTAINS “Some Name” RETURN o.Name AS org, c.Name AS country"""
query8 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
WHERE c.Name = “Afghanistan”
RETURN o.Name AS org, a.Name AS name"""
query9 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
WHERE o.Name = “Taliban”
RETURN c.Name AS country, a.Name AS name"""
query10 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
WHERE c.Name = “Afghanistan” AND o.Name = “Taliban”
RETURN a.Name AS name"""
query11 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
WHERE o.Name = “Taliban” AND a.AliasList CONTAINS “Some Name”
RETURN c.Name AS country"""
query12 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
WHERE c.Name = “Afghanistan” AND a.AliasList CONTAINS “Some Name”
RETURN o.Name AS org"""
query13 = """MATCH (a:AgentName)-[:AgentAlias]->(n:Aliases), (a:AgentName)-[:Sector]->(s1:Sector), (s1:Sector)-[:is-a]->(s2:Sector)
WHERE n.AliasList CONTAINS “Some Name” RETURN s1.Name + s2.Name AS desc"""
query14 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o:Organization)
WHERE “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN o.Name AS org, c.Name AS country, a.Name as name"""
query15 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o:Organization)
WHERE a.AliasList CONTAINS “Some Name” AND “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN o.Name AS org, c.Name AS country"""
query16 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
WHERE c.Name = “Afghanistan” AND “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN o.Name AS org, a.Name AS name"""
query17 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
WHERE o.Name = “Taliban” AND “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN c.Name AS country, a.Name AS name"""
query18 = """MATCH WHERE
(a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
c.Name = “Afghanistan” AND o.Name = “Taliban” AND “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN a.Name AS name"""
query19 = """MATCH WHERE
(a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
o.Name = “Taliban” AND
a.AliasList CONTAINS “Some Name” AND “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN c.Name AS country"""
query20 = """MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
WHERE c.Name = “Afghanistan” AND a.AliasList CONTAINS “Some Name” AND “2015-01-02”>= aff.beginDate AND “2015-01-02”<= aff.endDate
RETURN o.Name AS org"""


