from datalog import *
from datalogTestQueries import *
from query_Execution_Joins import *
from julius_test import *


print "General Parser Test"

for q in datalog_queries:
    inspect(q)

print "Parser Test With Actual Datalog Input Queries"

print datalog_queries.values

for q in datalog_queries:
    inspect(datalog_queries)

"Test Query Execution Engine that uses Datalog Parser as Base Classes"

return_tables, return_cols  = return_join_tables_cols(query8)
unorderd_return_df = return_schema_A_or_B_dfs(return_tables, return_cols)
Participants, ParticipantDetail = order_to_global_schema(unorderd_return_df)

print query8, "\n"
print "Tables:", return_tables, "Columns:", return_cols, "\n"
print unorderd_return_df.columns, "\n"
print Participants, ParticipantDetail

