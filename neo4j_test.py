from py2neo import authenticate, Graph
import pandas as pd
from pandas.util.testing import assert_frame_equal
from query_Execution_Joins import *

# IN CASE YOU HAVEN'T USED PYTEST BEFORE
# install pytest - "pip install pytest" should work
# from the command line, navigate to the folder
# run "py.test neo4j_test.py" from command line
# once all 3 tests pass, you're good

authenticate("54.85.112.231:7474", "neo4j", "LEbKqX3q")
graph = Graph("bolt://54.85.112.231/db/data/")




def test_one():
    """Return all of the associations of Ariel Sharon """

    # this is the query that your wrapper should parse and return from
    datalog_query = """
    q(organization) :-
    actor(id, _, pname, _),
    affiliation(id, organization, _, _),
    pname = 'Ariel Sharon'
    """

    # i am using your execute function to run the query above
    datalog_result = execute_query(datalog_query)

    # this is what i would expect your parser to ask the database
    neo_query = """
    Match (a: Actor {Name: 'Ariel Sharon'})-[aff:Affiliation]->(r)
    return r.Name as organization
    """

    # this is the result of the above query
    neo_result = graph.data(neo_query)
    neo_df = pd.DataFrame(neo_result)

    # this is what pytest uses to determine if the test passes.  I'm using basically comparing the result of your
    # wrapper and what I'd expect the result to be
    assert_frame_equal(neo_df, datalog_result)


# def test_two():
#     """Report the actor with highest number of affiliations, and how many affiliations they have."""
#     datalog_query = """
#     q(name, cnt) :-
#     actor(id, _, name, _),
#     affiliation(id, organization, _, _),
#     GROUP_BY([name], cnt = COUNT(organization)),
#     SORT_BY([cnt], 'DESC'),
#     LIMIT(1)
#     """
#
#     datalog_result = execute_query(datalog_query)
#
#     neo_query = """
#     Match (actor:Actor)-[aff:Affiliation]->(r)
#     WITH actor, count(aff) as cnt
#     RETURN actor.Name as name, cnt
#     ORDER BY cnt DESC, actor.Name
#     LIMIT 1
#     """
#
#     neo_result = graph.data(neo_query)
#     neo_df = pd.DataFrame(neo_result)
#
#     assert_frame_equal(neo_df, datalog_result)
#
#
# def test_three():
#     """Return the people associated for organization X.  Example X = 'Taliban'"""
#     datalog_query = """
#     q(name) :-
#     actor(id, _, name, _),
#     affiliation(id, 'Taliban', _, _)
#     """
#
#     datalog_result = execute_query(datalog_query)
#
#     neo_query = """
#     MATCH (o: Organization {Name: 'Taliban'})-[]-(p:Actor)
#     RETURN p.Name as name
#     """
#
#     neo_result = graph.data(neo_query)
#     neo_df = pd.DataFrame(neo_result)
#
#     assert_frame_equal(neo_df, datalog_result)
