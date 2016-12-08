from datalog import *
from datalogTestQueries import *
import pandas

#Reads data from the compressed HDF File
actor = pandas.read_hdf("Neo4JRelational.hdf", "Actor")
_from = pandas.read_hdf("Neo4JRelational.hdf", "From")
affiliation = pandas.read_hdf("Neo4JRelational.hdf", "Affiliation")
agentname = pandas.read_hdf("Neo4JRelational.hdf", "AgentName")
agenttype = pandas.read_hdf("Neo4JRelational.hdf", "AgentType")
aliases = pandas.read_hdf("Neo4JRelational.hdf", "Aliases")
agentsector = pandas.read_hdf("Neo4JRelational.hdf", "AgentSector")
sectorname = pandas.read_hdf("Neo4JRelational.hdf", "SectorName")
sectoris_a = pandas.read_hdf("Neo4JRelational.hdf", "SectorIs_A")


#Joines Pandas in to 2 Major Tables, Schema A & Schema B
schema_a1 = pandas.merge(actor, _from ,on='id')
schema_a = pandas.merge(schema_a1, affiliation, on='id')
schema_b1 = pandas.merge(agentname, agenttype ,on='id')
schema_b2 = pandas.merge(aliases, schema_b1, on='id' )
schema_b3 = pandas.merge(agentsector, schema_b2, on='id' )
schema_b4 = pandas.merge(sectorname, schema_b3, on='sector_id' )
schema_b = pandas.merge(sectoris_a, schema_b4, on='sector_id' )


def return_join_tables_cols(query):
    #This function returns the columns that need to be retrieved from either A or B of neo4J schema
    d = Datalog(query)
    columns = []
    tables = []

    #loops through tables and attributes and pulls data from non join key columns
    for x in d.relations:
        for a in x.attributes:
            # if x.attributes[a].isJoinPart == False:
            columns.append(x.attributes[a].name)
            tables.append(x.name)

    #gets unique values for columns and tables
    columns = list(set(columns))
    tables = list(set(tables))

    #Returns non join columns and list of tables that need to be returned in the query
    print "Return head:", d.head, "Projection:", d.getList
    return tables, columns, d.getList


def return_schema_A_or_B_dfs(tables, columns):
    #function returns query values in unordered dataframe

    #Gets available tables and columns list from schema A
    schemaA_tables = ['actor', 'from', 'affiliation']
    schemaA_col = schema_a.columns

    #Gets available tables and columns list from schema B
    schemaB_tables = ['agentname', 'agenttype', 'liases', 'agentsector', 'sectorname', 'sectoris_a']
    schemaB_col = schema_b.columns

    # Checks how many tables intersect
    tableA_intersect = [val for val in return_tables if val in schemaA_tables]
    tableB_intersect = [val for val in return_tables if val in schemaB_tables]

    # Checks how many columns intersect
    colA_intersect = [val for val in return_cols if val in schemaA_col]
    colB_intersect = [val for val in return_cols if val in schemaB_col]

    #Decides which schema and creates pandas dataframe of values that need to be returned
    if len(tableA_intersect) > len(tableB_intersect):
        return_df_unordered = schema_a[colA_intersect]
        print "Data is in Neo4J Schema A"
        return return_df_unordered

    elif len(tableA_intersect) < len(tableB_intersect):
        return_df_unordered = schema_b[colB_intersect]
        print "Data is in Neo4J Schema B"
        return return_df_unordered
    else:
        print "Columns being passed are not correct"

def projected_data_output(unorderd_return_df):
    return_projection_df = unorderd_return_df.reindex(columns=list(projection))
    return return_projection_df


return_tables, return_cols, projection = return_join_tables_cols(query8)
unorderd_return_df = return_schema_A_or_B_dfs(return_tables, return_cols)
print projected_data_output(unorderd_return_df)



# print query8, "\n"
# print "Tables:", return_tables, "Columns:", return_cols, "\n"
# print unorderd_return_df.columns, "\n"


#This is a test of the code above to show how it works!!!


