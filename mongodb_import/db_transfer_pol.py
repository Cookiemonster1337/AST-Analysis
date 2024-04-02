from pymongo import MongoClient

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_tb = sorted([t for t in test_list if t.endswith('TB')])

t = 1
for test in test_list_tb:
    print(str(test)[:-3])
    if str(test)[:-3] + '_CHAR' in db.list_collection_names():
        print('collection already exists!')
        continue
    else:
        collection = db[test]
        pol_collection_name = str(test)[:-2] + 'CHAR'
        print(str(pol_collection_name))

        pol_collection = db[pol_collection_name]
        print('Collection: ' + str(collection))

        query = {'File Mark': {'$in': ['pol', 'hfr', 'eis']}}
        projection = {
            #   'datetime_1': 1,
            # 'current_1': 1,
            # 'voltage_1': 1,
            # 'variable_08_1': 1,
        }

        entries = list(collection.find(query, projection))
        print('query data...')

        pol_collection.insert_many(entries)

    print('data transfer successfull for' + str(t) + '!')
