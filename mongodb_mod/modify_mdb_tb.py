#TODO: Import with forward-fill
#todo import in char_collections at same time

# from pymongo import MongoClient
# from datetime import datetime
# import pandas as pd
#
# client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
# db = client.dep6_gtb
#
# test_list = db.list_collection_names()
# test_list_cv = [t for t in test_list if t.endswith('TB')]
# print(test_list_cv)
#
# collections = test_list_cv
#
# for coll in collections:
#     collection = db[coll]
#
#     query = {'FileMark':'STARTUP_CYCLE-I'}
#     projection = {'datetime':1}
#
#     cursor = collection.find(query)
#     data = list(cursor)
#     data_df = pd.json_normalize(data)
#
#     dates = data_df['datetime'].unique()
#
#     for date in dates:
#
#         print(date)
#
# client.close()