import pandas as pd
import os
from pymongo import MongoClient
from datetime import datetime


client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

data_folder = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study'

tests = [t for t in os.listdir(data_folder)]

for t in tests:
    cv_data = '/'.join([data_folder, t, 'gamry/cv'])
    cv_files = [f for f in os.listdir(cv_data) if f.endswith('.DTA')]
    collection = db[t+'_CV']

    for cv_file in cv_files:

        if collection.find_one({'source_file': cv_file}):
            print('file already exists!')
            continue

        cv_file_data = '/'.join([data_folder, t, 'gamry/cv', cv_file])

        cv_df = pd.read_csv(cv_file_data, encoding='cp1252',
                             skiprows=64, sep='\t',
                             low_memory=False)

        cv_info_df = pd.read_csv(cv_file_data, encoding='cp1252',
                              nrows=12, sep='\t', low_memory=False)

        date = cv_info_df.iloc[2, 2]
        time = cv_info_df.iloc[3, 2]
        v_init = float(cv_info_df.iloc[7, 2])
        v_final = float(cv_info_df.iloc[10, 2])
        v_lim_1 = float(cv_info_df.iloc[8, 2])
        v_lim_2 = float(cv_info_df.iloc[9, 2])
        scanrate = float(cv_info_df.iloc[11, 2])

        cv_df = cv_df.rename(columns={'V vs. Ref.': 'v_vs_ref'})

        cv_df['date'] = date
        cv_df['time'] = time
        cv_df['v_init'] = v_init
        cv_df['v_final'] = v_final
        cv_df['v_limit_1'] = v_lim_1
        cv_df['v_limit_2'] = v_lim_2
        cv_df['scanrate'] = scanrate

        device = 'Gamry-I5000E'

        cv_df['datetime'] = datetime.strptime(date + ' ' + time, '%Y-%m-%d %I:%M:%S %p')

        cv_df['test_id'] = t
        cv_df['source_file'] = cv_file
        cv_df['device'] = device

        if (v_lim_1 == -0.9):
            cv_df['mode'] = 'cv'

        if (v_lim_1 == -0.3):
            cv_df['mode'] = 'lsv_p1'

        if (v_lim_1 == -0.5):
            cv_df['mode'] = 'lsv_p2'

        cv_dict = cv_df.to_dict(orient='records')

        collection.insert_many(cv_dict)
        print(cv_file + ' added to database')





