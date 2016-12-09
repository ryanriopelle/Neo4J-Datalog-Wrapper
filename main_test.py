from query_Execution_Joins import *


datalog_queries = [query5, query6, query7, query8, query9, query10]

print "Parser Test With Actual Datalog Input Queries"

for q in datalog_queries:
    print "For Query Below, Inspect:", q, "\n"
    inspect(q)

print "Test Query Execution Engine: (uses Datalog Parser as Base Classes)"

#Test 1
print execute_query(query6)

#Test 2
print execute_query(query7)

#Test 3
print execute_query(query8)

#test 4
print execute_query(query9)

#test 5
print execute_query(query10)
