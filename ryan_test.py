from datalog import *
from datalogTestQueries import *


#Creates pandas dictionary of tables as keys and values as columns
def dict_dfs(query):
    #print list_pandas.sort(key=lambda x: x[0])
    pandas_dict = {}
    d = Datalog(query)
    for x in d.relations:
        for a in x.attributes:
            if x.attributes[a].isJoinPart == True:
                if x.name in pandas_dict:
                    pandas_dict[x.name].append(x.attributes[a].name)
                else:
                    pandas_dict[x.name] = [x.attributes[a].name]
    return pandas_dict

dict_df = dict_dfs(datalog_queries[8])
print dict_df


# This function takes the keys in a dictionary and reduces based on join keys
while True:
    for i in list(dict_df):
        print "key: ", i
        print "value: ", dict_df[i]

        #Build new dict without old key
        new_dict = {key: value for key, value in dict_df.items() if key not in i}
        print "new_dict", new_dict

        #get another dataframe with matching keys
        related_key = list(new_dict.keys())[list(new_dict.values()).index(dict_df[i])]
        print "Related Key:", related_key, "\n"



        dict_df.pop(i)
        if len(dict_df)<=0:
            break
#
#
#
# def create_df_list(datalog_query):
#
#     #Creates unordered list of dataframes to be joined from Neo4J relational DB
#     df_list=[]
#     d = Datalog(datalog_query)
#     for x in d.relations:
#         for a in x.attributes:
#             if x.attributes[a].isJoinPart == True:
#                 # print  x.name , x.attributes[a].name , x.attributes[a].index
#                 df_list.append([x.name , [x.attributes[a].name]])
#     return df_list
#
# # list_pandas = create_df_list(query8)
# # print list_pandas
#
# # def sort_frames(df_list):
# #
# #     #sorts list for further processing joins
# #     sorted_df_list = sorted(df_list, key=lambda row: row[1][0], reverse=True)
# #     return sorted_df_list
# #
# # print create_df_list(datalog_queries[5])
#
# #
# # #Pulls the names of the dataframes that need to be sorted with join key info
# # df_names =  create_df_list(datalog_queries[5])
# #
# # #Sorts the list of dataframes by the join key
# # names_sorted_by_key = sort_frames(df_names)
# #
# # #Sets up data structure to hold dataframes with key info
# # df_list_with_keys = names_sorted_by_key
#
#
#
#
#
# # for df_names in df_list_with_keys:
# #     df_names[0] = vars().get(df_names[0])
# #
# #
# # print names_sorted_by_key[0]
# # i=0
# #
# # for keys in df_list_with_keys:
# #
# #     key = df_list_with_keys[i][1][0]
# #     print "for key", key
# #     if i == 0:
# #         pass
# #     else:
# #         if df_list_with_keys[i][1][0] == df_list_with_keys[i-1][1][0]:
# #             joined_table = pandas.merge(df_list_with_keys[i][0], df_list_with_keys[i-1][0],\
# #                                         on=key)
# #     i+=1
# #
# # print joined_table
# #
# #
# joined_check = pandas.merge(names_sorted_by_key[0[0]],AgentName,on='id')



##  This reorder the dataframe to the same order as the global dataframes
# def order_to_global_schema(unorderd_return_df):
#
#     #The following three lines describe the global schema
#     ParticipantsGlobalSchema = ['_0', 'id', '_2', 'ptype', 'pname', 'sector_id']
#     ParticipantDetailGlobalSchema = ['_0', 'Category', 'org', 'country', 'name', '_5']
#     Events = ['Date']
#
#     #Set empty dataframes
#     Participants = pandas.DataFrame(columns=ParticipantsGlobalSchema)
#     ParticipantDetail = pandas.DataFrame(columns=ParticipantDetailGlobalSchema)
#     Events = pandas.DataFrame(columns=Events)
#
#     #checks if the input df has columns in Participants Global Schema Return Table
#     if len([val for val in unorderd_return_df.columns if val in ParticipantsGlobalSchema]) > 0:
#         Participants = unorderd_return_df.reindex(columns=list(ParticipantsGlobalSchema))
#     else:
#         pass
#
#     # checks if the input df has columns in ParticipantDetail Global Schema Return Table
#     if len([val for val in unorderd_return_df.columns if val in ParticipantDetailGlobalSchema]) > 0:
#         ParticipantDetail = unorderd_return_df.reindex(columns=list(ParticipantDetailGlobalSchema))
#     else:
#         pass
#
#     return Participants,ParticipantDetail