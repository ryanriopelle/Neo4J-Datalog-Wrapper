from Datalog import *
#
# dfs = [df0, df1, df2, dfN]
#
# df_final = reduce(lambda left,right: pd.merge(left,right,on='name'), dfs)
#
# for x in d.relations:
# #     print x.name



# inspect(query5)


list_pandas=[]
d = Datalog(datalog_queries[5])
for x in d.relations:
    for a in x.attributes:
        if x.attributes[a].isJoinPart == True:
            # print  x.name , x.attributes[a].name , x.attributes[a].index
            list_pandas.append([x.name , [x.attributes[a].name , x.attributes[a].index]])

print list_pandas.sort(key=lambda x: x[0])

# pandas_dict = {}
# d = Datalog(datalog_queries[5])
# for x in d.relations:
#     for a in x.attributes:
#         if x.attributes[a].isJoinPart == True:
#             if x.name in pandas_dict:
#                 pandas_dict[x.name].append([x.attributes[a].name , x.attributes[a].index])
#             else:
#                 pandas_dict[x.name] = [[x.attributes[a].name, x.attributes[a].index]]
# print pandas_dict

fdgfgf