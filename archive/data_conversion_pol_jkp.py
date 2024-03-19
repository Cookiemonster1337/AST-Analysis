
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import os

select_dir = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\AST Study\ast1_uncoated_#01\logs'

csv_files = [f for f in os.listdir(select_dir) if f.endswith('.csv')]
test_data_dfs = {}

columns_of_interest = ['Time Stamp', 'voltage', 'current', 'File Mark',
                       'variable_16', 'current_set']

i = 1
for file in csv_files:
    df_file = pd.read_csv(os.path.join(select_dir, file), encoding='cp1252', skiprows=17, usecols=columns_of_interest,
                          low_memory=False)

    df_file = df_file.sort_values(by='Time Stamp', ascending=True)

    test_data_dfs[file] = df_file

    print(str(i) + 'of' + str(len(csv_files)))
    i += 1

test_data_df = pd.concat(test_data_dfs.values(), ignore_index=True)

print(test_data_df['File Mark'].unique())

test_data_df['File Mark'].fillna(method='ffill', inplace=True)

test_data_df = test_data_df[test_data_df['File Mark'].str.contains('pol', na=False)]

test_data_df.to_csv(r'C:\Users\j.kapp\PycharmProjects\in-situ-pemfc-GL\data\#001_ast#01_uncoated\pol.csv',
                    index=False)