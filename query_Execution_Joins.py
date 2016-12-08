from datalog import *
from datalogTestQueries import *
import pandas

#Reads data from the compressed HDF File
Actor = pandas.read_hdf("Neo4JRelational.hdf", "Actor")
From = pandas.read_hdf("Neo4JRelational.hdf", "From")
Affiliation = pandas.read_hdf("Neo4JRelational.hdf", "Affiliation")
AgentName = pandas.read_hdf("Neo4JRelational.hdf", "AgentName")
AgentType = pandas.read_hdf("Neo4JRelational.hdf", "AgentType")
Aliases = pandas.read_hdf("Neo4JRelational.hdf", "Aliases")
AgentSector = pandas.read_hdf("Neo4JRelational.hdf", "AgentSector")
SectorName = pandas.read_hdf("Neo4JRelational.hdf", "SectorName")
SectorIs_A = pandas.read_hdf("Neo4JRelational.hdf", "SectorIs_A")


#Joines Pandas in to 2 Major Tables, Schema A & Schema B
Schema_a1 = pandas.merge(Actor, From ,on='id')
Schema_A = pandas.merge(Schema_a1, Affiliation, on='id')
Schema_b1 = pandas.merge(AgentName, AgentType ,on='id')
Schema_b2 = pandas.merge(Aliases, Schema_b1, on='id' )
Schema_b3 = pandas.merge(AgentSector, Schema_b2, on='id' )
Schema_b4 = pandas.merge(SectorName, Schema_b3, on='sector_id' )
Schema_B = pandas.merge(SectorIs_A, Schema_b4, on='sector_id' )



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
    return tables, columns


#
def return_schema_A_or_B_dfs(tables, columns):
    #function returns query values in unordered dataframe

    #Gets available tables and columns list from schema A
    schemaA_tables = ['Actor', 'From', 'Affiliation']
    schemaA_col = Schema_A.columns

    #Gets available tables and columns list from schema B
    schemaB_tables = ['AgentName', 'AgentType', 'liases', 'AgentSector', 'SectorName', 'SectorIs_A']
    schemaB_col = Schema_B.columns

    # Checks how many tables intersect
    tableA_intersect = [val for val in return_tables if val in schemaA_tables]
    tableB_intersect = [val for val in return_tables if val in schemaB_tables]

    # Checks how many columns intersect
    colA_intersect = [val for val in return_cols if val in schemaA_col]
    colB_intersect = [val for val in return_cols if val in schemaB_col]

    #Decides which schema and creates pandas dataframe of values that need to be returned
    if len(tableA_intersect) > len(tableB_intersect):
        return_df_unordered = Schema_A[colA_intersect]
        print "Data is in Neo4J Schema A"
        return return_df_unordered

    elif len(tableA_intersect) < len(tableB_intersect):
        return_df_unordered = Schema_B[colB_intersect]
        print "Data is in Neo4J Schema B"
        return return_df_unordered
    else:
        print "Columns being passed are not correct"


def order_to_global_schema(unorderd_return_df):

    #The following three lines describe the global schema
    ParticipantsGlobalSchema = ['_0', 'id', '_2', 'ptype', 'pname', 'sector_id']
    ParticipantDetailGlobalSchema = ['_0', 'Category', 'org', 'country', 'name', '_5']
    Events = ['Date']

    #Set empty dataframes
    Participants = pandas.DataFrame(columns=ParticipantsGlobalSchema)
    ParticipantDetail = pandas.DataFrame(columns=ParticipantDetailGlobalSchema)
    Events = pandas.DataFrame(columns=Events)

    #checks if the input df has columns in Participants Global Schema Return Table
    if len([val for val in unorderd_return_df.columns if val in ParticipantsGlobalSchema]) > 0:
        Participants = unorderd_return_df.reindex(columns=list(ParticipantsGlobalSchema))
    else:
        pass

    # checks if the input df has columns in ParticipantDetail Global Schema Return Table
    if len([val for val in unorderd_return_df.columns if val in ParticipantDetailGlobalSchema]) > 0:
        ParticipantDetail = unorderd_return_df.reindex(columns=list(ParticipantDetailGlobalSchema))
    else:
        pass

    return Participants,ParticipantDetail



#This is a test of the code above to show how it works!!!

# return_tables, return_cols  = return_join_tables_cols(query8)
# unorderd_return_df = return_schema_A_or_B_dfs(return_tables, return_cols)
# Participants, ParticipantDetail = order_to_global_schema(unorderd_return_df)
#
# print query8, "\n"
# print "Tables:", return_tables, "Columns:", return_cols, "\n"
# print unorderd_return_df.columns, "\n"
# print Participants, ParticipantDetail