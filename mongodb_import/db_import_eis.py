import pandas as pd
import os
from pymongo import MongoClient
from datetime import datetime


client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

data_folder = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study'

tests = [t for t in os.listdir(data_folder)]

for t in tests:
    eis_data = '/'.join([data_folder, t, 'gamry/eis'])
    eis_files = [f for f in os.listdir(eis_data) if f.endswith('.DTA')]
    collection = db[t+'_EIS']

    for eis_file in eis_files:

        if collection.find_one({'source_file': eis_file}):
            print('file already exists!')
            continue

        eis_file_data = '/'.join([data_folder, t, 'gamry/eis', eis_file])

        eis_df = pd.read_csv(eis_file_data, encoding='cp1252',
                              skiprows=54, sep='\t',
                              low_memory=False)

        info_df = pd.read_csv(eis_file_data, encoding='cp1252',
                              nrows=12, sep='\t', low_memory=False)

        amp = float(info_df.iloc[11, 2])
        freq_final = float(info_df.iloc[9, 2])

        date = info_df.iloc[2, 2]
        time = info_df.iloc[3, 2]

        eis_df = eis_df.rename(columns={'ohm': 'z_real', 'ohm.1': 'z_imag'})

        device = 'Gamry-I5000E'

        eis_df['datetime'] = datetime.strptime(date + ' ' + time, '%Y-%m-%d %I:%M:%S %p')

        eis_df['test_id'] = t
        eis_df['source_file'] = eis_file
        eis_df['device'] = device
        eis_df['starttime'] = time

        if (freq_final == 10000):
            eis_df['mode'] = 'hfr'

        if (freq_final == 0.1):
            eis_df['mode'] = 'char'

        eis_dict = eis_df.to_dict(orient='records')

        collection.insert_many(eis_dict)
        print(eis_file + ' added to database')



