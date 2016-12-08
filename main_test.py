from datalog import *
from datalogTestQueries import *
from query_Execution_Joins import *
from julius_test import *

datalog_queries = [query5, query6, query7, query8]

print "Parser Test With Actual Datalog Input Queries"

for q in datalog_queries:
    print "For Query Below, Inspect:", q, "\n"
    inspect(q)

"Test Query Execution Engine that uses Datalog Parser as Base Classes"

return_tables, return_cols, projection = return_join_tables_cols(query8)
unorderd_return_df = return_schema_A_or_B_dfs(return_tables, return_cols)


print query8, "\n"
print "Tables:", return_tables, "Columns:", return_cols, "\n"
print projected_data_output(unorderd_return_df)

