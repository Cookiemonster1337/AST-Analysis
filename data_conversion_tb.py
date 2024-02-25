
import pandas as pd
import os

sample= 'ast1_coated_#01'

dir_source = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study' + '\\'  + sample +'\logs'
dir_target = r'C:\Users\j.kapp\PycharmProjects\in-situ-pemfc-GL\data' + '\\' + sample

csv_files = [f for f in os.listdir(dir_source) if f.endswith('.csv')]

test_data_all_dfs = {}
test_data_dfs = {}

columns_of_interest = ['Time Stamp',
                       'voltage',
                       'current',
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
    df_file = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252', skiprows=17, usecols=columns_of_interest,
                          low_memory=False)

    df_file['File Mark'].fillna(method='ffill', inplace=True)

    rows_to_drop = [i for i in range(1, len(df_file)) if i % 60 != 0]

    test_data_all_dfs[file] = df_file

    test_data_dfs[file] = df_file.drop(index=rows_to_drop)

    print(str(i) + 'of' + str(len(csv_files)))

    i += 1

test_data_df = pd.concat(test_data_dfs.values(), ignore_index=True)
test_data_all_df = pd.concat(test_data_all_dfs.values(), ignore_index=True)

test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)
test_data_all_df = test_data_all_df.sort_values(by='Time Stamp', ascending=True)

test_data_df.to_csv(dir_target + '\summary_60s.csv', index=False)
test_data_all_df.to_csv(dir_target + '\summary.csv', index=False)
