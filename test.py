from pymongo import MongoClient
import pandas as pd
import time

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

start = time.time()

collection = db['001_ast01_uncoated_01_TB']
print('Collection: ' + str(collection))

query = {'FileMark_text': {'$in': ['polcurve', 'hfr', 'eis']}}
projection = {'datetime_1': 1,
              'current_1': 1,
              'voltage_1': 1,
              'variable_08_1': 1,
              }

cursor = collection.find(query, projection)
print('query data...')

plot_data = list(cursor)
pol_df = pd.json_normalize(plot_data)
end_df = time.time()
elapsed_time = end_df-start
print('runtime: ' + str(elapsed_time))
print('data query successfull')