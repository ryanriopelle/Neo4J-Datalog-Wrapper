from Relational_To_Parser import *


def create_df_list(datalog_query):

    #Creates unoered list of dataframes to be joined from Neo4J relational DB
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
print sorted_df_list

print AgentType[0]
# print AgentName
# type(AgentType[0])
# print type(AgentName[0])
# pandas.merge(AgentType[0],AgentName[0],on='sid')


#reduce(lambda left,right: pandas.merge(AgentType[0],AgentName[0],on='sid'), sorted_df_list)


# # Joins multiple dataframes
# df_final = reduce(lambda left,right: pd.merge(left,right,on='name'), sorted_df_list)
#


#
# for x in d.relations:
#     print x.name