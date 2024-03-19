import pandas as pd
import os
from pymongo import MongoClient

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

data_folder = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study'

tests = [t for t in os.listdir(data_folder)]

testloop = 0
for t in tests:
    testloop += 1
    tb_data = '/'.join([data_folder, t, 'logs'])
    log_files = [f for f in os.listdir(tb_data) if f.endswith('.csv')]

    collection = db[t]

    loop = 0
    for log in log_files:
        loop += 1
        if collection.find_one({'source_file': log}):
            continue
        else:
            info_df = pd.read_csv(os.path.join(tb_data, log), encoding='cp1252', nrows=16, low_memory=False)
            device = info_df[info_df['Format'] == 'Station ID']['1'].iloc[0]
            start = info_df[info_df['Format'] == 'Start Time']['1'].iloc[0]

            log_df = pd.read_csv(os.path.join(tb_data, log), encoding='cp1252', skiprows=17, low_memory=False)

            log_df['datetime'] = pd.to_datetime(log_df['Time Stamp'])

            log_df['test_id'] = t
            log_df['source_file'] = log
            log_df['device'] = device
            log_df['starttime'] = start

            log_dict = log_df.to_dict(orient='records')

            print(str(loop) + 'of' + str(len(log_files)) + ' , ' + str(testloop) + 'of' + str(len(tests)))

            collection.insert_many(log_dict)


