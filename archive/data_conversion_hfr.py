
import pandas as pd
import os
import math

dir_source = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study\ast1_coated_#01\gamry\eis'
dir_target = r'C:\Users\j.kapp\PycharmProjects\in-situ-pemfc-GL\data\#002_ast#01_coated'

csv_files = [f for f in os.listdir(dir_source)]

hfr_dfs = {}

columns_of_interest = ['s', 'Hz', 'ohm', 'ohm.1', '°']

for file in csv_files:
    df_file = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252',
                          skiprows=54, sep='\t', usecols=columns_of_interest,
                          low_memory=False)

    df_info = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252',
                          nrows=12, sep='\t', low_memory=False)

    amp = float(df_info.iloc[11, 2])
    freq_final = float(df_info.iloc[9, 2])

    date = df_info.iloc[2, 2]
    time = df_info.iloc[3, 2]

    df_file['amp'] = amp
    df_file['date'] = date
    df_file['time'] = time

    print(str(amp), str(freq_final))

    if freq_final == 100:
        print('HFR (' + str(amp * 20) + ')' + ' ' + str(date) + ' ' + str(time))
        df_file['current'] = math.ceil((amp * 20) / 2.5) * 2.5
        hfr_dfs[file] = df_file

hfr_df = pd.concat(hfr_dfs.values(), ignore_index=True)

hfr_df.to_csv(dir_target + '\hfr.csv', index=False)








