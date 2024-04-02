import pandas as pd
import os
from pymongo import MongoClient

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

data_folder = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study'

tests = [t for t in os.listdir(data_folder)]

testloop = 0
for t in tests:
    print(t)
    if t+'_TB' in db.list_collection_names():
        print('collection already exists!')
        continue
    else:
        testloop += 1
        tb_data = '/'.join([data_folder, t, 'logs'])
        log_files = [f for f in os.listdir(tb_data) if f.endswith('.csv')]

        collection = db[t+'_TB']

        loop = 0

        log_dfs = {}

        filemark = None

        for log in log_files:
            print(str(loop) + 'of' + str(len(log_files)) + ' , ' + str(testloop) + 'of' + str(len(tests)))
            print(log)
            loop += 1
            if collection.find_one({'source_file': log}):
                continue
            else:
                info_df = pd.read_csv(os.path.join(tb_data, log), encoding='cp1252', nrows=16, low_memory=False)
                device = info_df[info_df['Format'] == 'Station ID']['1'].iloc[0]
                start = info_df[info_df['Format'] == 'Start Time']['1'].iloc[0]

                log_df = pd.read_csv(os.path.join(tb_data, log), encoding='cp1252', skiprows=17, low_memory=False)

                log_df.sort_values(by='Time Stamp', ascending=True)

                log_df = log_df.reset_index(drop=True)

                filemark = log_df['File Mark'].iloc[0]

                print(filemark)

                if isinstance(filemark, (str)):
                    pass
                else:
                    try:
                        log_df['File Mark'].iloc[0]= last_filemark
                    except NameError:
                        print('first filemark is nan')

                log_df['File Mark'].fillna(method='ffill', inplace=True)

                log_df['datetime'] = pd.to_datetime(log_df['Time Stamp'])

                log_df['test_id'] = t
                log_df['source_file'] = log
                log_df['device'] = device
                log_df['starttime'] = start

                last_filemark = log_df['File Mark'].iloc[-1]

            #     log_dfs[log] = log_df
            #
            #
            # log_data_df = pd.concat(log_dfs.values(), ignore_index=True)
                log_dict = log_df.to_dict(orient='records')
                collection.insert_many(log_dict)






