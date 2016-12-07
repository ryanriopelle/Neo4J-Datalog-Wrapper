




#
# query8 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
# WHERE c.Name = 'Afghanistan'
# RETURN o.Name AS org, a.Name AS name
# """
#
#
# query9 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
# WHERE o.Name = 'Taliban'
# RETURN c.Name AS country, a.Name AS name
# """
#
#
# query10 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
# WHERE c.Name = 'Afghanistan' AND o.Name = 'Taliban'
# RETURN a.Name AS name
# """
#
#
# query11 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
# WHERE o.Name = %group AND a.AliasList CONTAINS %some_name
# RETURN c.Name AS country
# """ %group %some_name
#
#
# query12 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[:Affiliation]->(o.Organization)
# WHERE c.Name = 'Afghanistan' AND a.AliasList CONTAINS %some_name
# RETURN o.Name AS org
# """ %some_name
#
#
# query13 = """
# MATCH (a:AgentName)-[:AgentAlias]->(n:Aliases), (a:AgentName)-[:Sector]->(s1:Sector), (s1:Sector)-[:is-a]->(s2:Sector)
# WHERE n.AliasList CONTAINS %some_name
# RETURN s1.Name + s2.Name AS desc
# """
#
#
# query14 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o:Organization)
# WHERE %date1>= aff.beginDate AND %date1<= aff.endDate
# RETURN o.Name AS org, c.Name AS country, a.Name as name
# """ %(date, date)
#
#
# query15 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o:Organization)
# WHERE a.AliasList CONTAINS %some_name AND '2015-01-02'>= aff.beginDate AND '2015-01-02'<= aff.endDate
# RETURN o.Name AS org, c.Name AS country
# """ %some_name
#
#
# query16 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
# WHERE c.Name = %country AND %date>= aff.beginDate AND %date<= aff.endDate
# RETURN o.Name AS org, a.Name AS name
# """ %(country, date, date)
#
#
# query17 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
# WHERE o.Name = %country AND %date>= aff.beginDate AND %date<= aff.endDate
# RETURN c.Name AS country, a.Name AS name
# """ %(country, date, date)
#
#
# query18 = """
# MATCH WHERE
# (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
# c.Name = %country AND o.Name = %org AND %date>= aff.beginDate AND %date <= aff.endDate
# RETURN a.Name AS name
# """ %(country, org, date, date)
#
#
# query19 = """
# MATCH WHERE
# (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
# o.Name = %org AND
# a.AliasList CONTAINS %some_name AND %date >= aff.beginDate AND %date<= aff.endDate
# RETURN c.Name AS country
# """ %(org, some_name, date, date)
#
#
# query20 = """
# MATCH (a:Actor)-[:From]->(c:Country), (a:Actor)-[aff:Affiliation]->(o.Organization)
# WHERE c.Name = %org AND a.AliasList CONTAINS %some_name AND %date>= aff.beginDate AND %date <= aff.endDate
# RETURN o.Name AS org
# """ %(org, some_name, date, date)