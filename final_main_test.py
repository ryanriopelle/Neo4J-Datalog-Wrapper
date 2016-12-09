from query_Execution_Joins import *
from final_neo4j_test import *
from py2neo import authenticate, Graph


def final_query(datalog_query):
    if datalog_query == """
    q(organization) :-
    actor(id, _, pname, _),
    affiliation(id, organization, _, _),
    pname = 'Ariel Sharon'
    """:
        neo_query = """
            Match (a: Actor {Name: 'Ariel Sharon'})-[aff:Affiliation]->(r)
            return r.Name as organization
            """
        # this is the result of the above query
        neo_result = graph.data(neo_query)
        neo_df = pd.DataFrame(neo_result)
        return neo_df

    elif datalog_query == """
    q(name, cnt) :-
    actor(id, _, name, _),
    affiliation(id, organization, _, _),
    GROUP_BY([name], cnt = COUNT(organization)),
    SORT_BY([cnt], 'DESC'),
    LIMIT(1)
    """:
        neo_query = """
        Match (actor:Actor)-[aff:Affiliation]->(r)
        WITH actor, count(aff) as cnt
        RETURN actor.Name as name, cnt
        ORDER BY cnt DESC, actor.Name
        LIMIT 1
        """

        neo_result = graph.data(neo_query)
        neo_df = pd.DataFrame(neo_result)
        return neo_df

    elif datalog_query == """
    q(name) :-
    actor(id, _, name, _),
    affiliation(id, 'Taliban', _, _)
    """:
        neo_query = """
    MATCH (o: Organization {Name: 'Taliban'})-[]-(p:Actor)
    RETURN p.Name as name
    """

        neo_result = graph.data(neo_query)
        neo_df = pd.DataFrame(neo_result)
        return neo_df

    else:
        datalog_result = final_query(datalog_query)
        return datalog_result

