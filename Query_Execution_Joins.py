from Datalog import *
from DatalogTestQueries import *
import pandas


Actor = pandas.read_hdf("Neo4JRelational.hdf", "Actor")
From = pandas.read_hdf("Neo4JRelational.hdf", "From")
Affiliation = pandas.read_hdf("Neo4JRelational.hdf", "Affiliation")
AgentName = pandas.read_hdf("Neo4JRelational.hdf", "AgentName")
AgentType = pandas.read_hdf("Neo4JRelational.hdf", "AgentType")
Aliases = pandas.read_hdf("Neo4JRelational.hdf", "Aliases")
AgentSector = pandas.read_hdf("Neo4JRelational.hdf", "AgentSector")
SectorName = pandas.read_hdf("Neo4JRelational.hdf", "SectorName")
SectorIs_A = pandas.read_hdf("Neo4JRelational.hdf", "SectorIs_A")


dataframes_names = ['Actor', 'From', 'Affiliation', 'AgentName', 'AgentType', \
              'Aliases', 'AgentSector', 'SectorName', 'SectorIs_A']

dataframes=[Actor, From, Affiliation, AgentName, AgentType, \
              Aliases, AgentSector, SectorName, SectorIs_A]


def create_df_list(datalog_query):

    #Creates unordered list of dataframes to be joined from Neo4J relational DB
    df_list=[]
    d = Datalog(datalog_query)
    for x in d.relations:
        for a in x.attributes:
            if x.attributes[a].isJoinPart == True:
                # print  x.name , x.attributes[a].name , x.attributes[a].index
                df_list.append([x.name , (x.attributes[a].name , x.attributes[a].index)])
    return df_list


def sort_frames(df_list):

    #sorts list for further processing joins
    sorted_df_list = sorted(df_list, key=lambda row: row[1][0], reverse=True)
    return sorted_df_list


df_list =  create_df_list(datalog_queries[3])
sorted_df_list = sort_frames(df_list)


# for df in dataframes:
#     print df.label
    # for df_name in sorted_df_list:
    #
    #     print vars([df])
    #     print locals(df)
    #         if str(df_name[0])==df:
    #             print df_name[0]
    #             df_name=df
    #         else:
    #             pass

print sort_frames(create_df_list(datalog_queries[1]))

# from DatalogTestQueries import *
# for q in datalog_queries:
#     inspect(q)


joined_check = pandas.merge(AgentType,AgentName,on='id')




#reduce(lambda left,right: pandas.merge(AgentType[0],AgentName[0],on='sid'), sorted_df_list)


# # Joins multiple dataframes
# df_final = reduce(lambda left,right: pd.merge(left,right,on='name'), sorted_df_list)

