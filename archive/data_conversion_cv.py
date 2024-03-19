
import pandas as pd
import os

dir_source = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study\ast2_coated_#01\gamry\cv'
dir_target = r'C:\Users\j.kapp\PycharmProjects\in-situ-pemfc-GL\data\#004_ast#02_coated'

csv_files = [f for f in os.listdir(dir_source)]

cv01_dfs = {}
cv02_dfs = {}
cv03_dfs = {}
cv04_dfs = {}

columns_of_interest = ['V vs. Ref.', 'A', '#.2']

cv01_counter = 1
cv02_counter = 1
cv03_counter = 1
cv04_counter = 1

for file in csv_files:
    df_file = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252',
                          skiprows=64, sep='\t', usecols=columns_of_interest,
                          low_memory=False)

    df_info = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252',
                          nrows=12, sep='\t', low_memory=False)

    date = df_info.iloc[2, 2]
    time = df_info.iloc[3, 2]
    v_low = float(df_info.iloc[8, 2])
    v_high = float(df_info.iloc[9, 2])
    scanrate = float(df_info.iloc[11, 2])

    df_file['date'] = date
    df_file['time'] = time
    df_file['v_low'] = v_low
    df_file['v_high'] = v_high
    df_file['scanrate'] = scanrate

    length = len(df_file)
    print(length)

    print(float(v_low), float(v_high), float(scanrate))

    if (v_high == 0.05) and (length < 5000):
        print('CV-Data (0.05-900mV @100mv/s) Files ' + str(cv01_counter))
        df_file['#'] = cv01_counter
        cv01_dfs[file] = df_file
        cv01_counter += 1

    if (v_high == 0) and (length < 5000):
        print('CV-Data (0.-900mV @100mv/s) Files ' + str(cv02_counter))
        df_file['#'] = cv02_counter
        cv02_dfs[file] = df_file
        cv02_counter += 1

    if (v_high == 0.05) and (length > 5000):
        print('CV-Data (0.05-900mV @20mv/s) Files ' + str(cv03_counter))
        df_file['#'] = cv03_counter
        cv03_dfs[file] = df_file
        cv03_counter += 1

    if (v_high == 0) and (length > 5000):
        print('CV-Data (0-900mV @20mv/s) Files ' + str(cv04_counter))
        df_file['#'] = cv04_counter
        cv04_dfs[file] = df_file
        cv04_counter += 1

try:
    cv01_df = pd.concat(cv01_dfs.values(), ignore_index=True)
except:
    print('No CV-Data for 0.05-900mV @100mVs')
try:
    cv02_df = pd.concat(cv02_dfs.values(), ignore_index=True)
except:
    print('No CV-Data for 0-900mV @100mVs')
try:
    cv03_df = pd.concat(cv03_dfs.values(), ignore_index=True)
except:
    print('No CV-Data for 0.05-900mV @20mVs')
try:
    cv04_df = pd.concat(cv04_dfs.values(), ignore_index=True)
except:
    print('No CV-Data for 0-900mV @20mVs')

try:
    cv01_df.to_csv(dir_target + '\cv_005-900_100mVs.csv', index=False)
except:
    pass
try:
    cv02_df.to_csv(dir_target + '\cv_0-900_100mVs.csv', index=False)
except:
    pass
try:
    cv03_df.to_csv(dir_target + '\cv_005-900_20mVs.csv', index=False)
except:
    pass
try:
    cv04_df.to_csv(dir_target + '\cv_0-900_20mVs.csv', index=False)
except:
    pass
