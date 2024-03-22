# from pymongo import MongoClient
#
# client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
# db = client.dep6_gtb
#
# test_list = db.list_collection_names()
# collections = [t for t in test_list
#                # if not t.endswith('EIS')
#                # and not t.endswith('CV')
#                # and not t.endswith('views')
#                if not t.endswith('views')
#                ]
#
# print(collections)
#
# for coll in collections:
#     new_coll_name = str(coll)[1:]
#     db[coll].rename(new_coll_name)
#
# client.close()

# cursor = collection.delete_many({})