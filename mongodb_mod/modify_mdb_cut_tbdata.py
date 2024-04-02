from pymongo import MongoClient
from datetime import datetime
import pandas as pd

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

collection = db['012_coated_post-corrosion_TB']
print(collection)

start_time = datetime(2024, 3, 1, 10, 50, 0)
end_time = datetime(2024, 3, 1, 19, 30, 0)
print(start_time, end_time)

query = {'datetime':{'$lt':start_time}}

collection.delete_many(query)
print('pre-start data cut!')

query = {'datetime':{'$gt':end_time}}

collection.delete_many(query)
print('post-end data cut!')