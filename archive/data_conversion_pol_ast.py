import pandas as pd
import numpy as np
import os

select_dir = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study\ast2_coated_#01\logs'

csv_files = [f for f in os.listdir(select_dir) if f.endswith('.csv')]
test_data_dfs = {}

columns_of_interest = ['Time Stamp',
                       'voltage',
                       'current',
                       'current_set',
                       'pressure_stack_compression',

                       # COOLANT
                       'temp_anode_endplate',
                       'temp_cathode_endplate',
                       'temp_coolant_inlet',
                       'temp_coolant_outlet',
                       'temp_coolant_in_out_diff',
                       'pressure_coolant_inlet',
                       'pressure_coolant_outlet',
                       'pressure_coolant_in_out_diff',

                       # ANODE
                       'anode_stoich',
                       'anode_inlet_rel_hum',
                       'temp_anode_inlet',
                       'temp_anode_outlet',
                       'temp_anode_in_out_diff',
                       'pressure_anode_inlet',
                       'pressure_anode_outlet',
                       'pressure_anode_in_out_diff',

                       # CATHODE
                       'cathode_stoich',
                       'cathode_inlet_rel_hum',
                       'temp_cathode_inlet',
                       'temp_cathode_outlet',
                       'temp_cathode_in_out_diff',
                       'pressure_cathode_inlet',
                       'pressure_cathode_outlet',
                       'pressure_cathode_in_out_diff',
                       'total_anode_stack_flow',
                       'total_cathode_stack_flow',

                       'File Mark',
                       'variable_01', 'variable_01', 'variable_02',
                       'variable_03', 'variable_04', 'variable_05', 'variable_06',
                       'variable_07', 'variable_08', 'variable_09', 'variable_10',
                       'variable_11', 'variable_12', 'variable_13', 'variable_14',
                       'variable_15', 'variable_16', 'variable_17', 'variable_18',
                       'variable_19', 'variable_20']

i = 1
for file in csv_files:
    df_file = pd.read_csv(os.path.join(select_dir, file), encoding='cp1252', skiprows=17, usecols=columns_of_interest,
                          low_memory=False)

    df_file = df_file.sort_values(by='Time Stamp', ascending=True)

    test_data_dfs[file] = df_file

    print(str(i) + 'of' + str(len(csv_files)))
    i += 1

test_data_df = pd.concat(test_data_dfs.values(), ignore_index=True)

test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

test_data_df = test_data_df.reset_index(drop=True)

test_data_df.loc[:, 'variable_20'] = np.nan

cyclestarts = test_data_df[test_data_df['File Mark'].str.contains('polcurve_dec_01', na=False)].index.tolist()

x = 1
for c in cyclestarts:
    print(c, x)
    test_data_df.loc[c, 'variable_20'] = x
    x += 1

test_data_df['File Mark'].fillna(method='ffill', inplace=True)
test_data_df['variable_20'].fillna(method='ffill', inplace=True)

test_data_df = test_data_df[test_data_df['File Mark'].str.contains('polcurve|hfr|eis', na=False)]

test_data_df.to_csv(
    r'C:\Users\j.kapp\PycharmProjects\in-situ-pemfc-GL\data\#004_ast#02_coated\pol.csv',
    index=False)