from pymongo import MongoClient

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_eis = [t for t in test_list if t.endswith('EIS')]

collections = test_list_eis

for coll in collections:
    collection = db[coll]
    cursor = collection.delete_many({})

client.close()