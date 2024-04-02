# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 07:41:52 2024

@author: j.kapp
"""

from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

palette = px.colors.qualitative.Bold

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_char = sorted([t for t in test_list if t.endswith('EIS')])

traces = []
c = 0

for test in test_list_char:
    print(test)
    collection = db[test]

    query = {'mode': 'char'}
    projection = {'#': 1, 'z_real': 1, 'z_imag': 1, 'ac_amp': 1, 'datetime': 1, 'Hz': 1, 'source_file': 1}

    cursor = collection.find(query, projection)

    plot_data = list(cursor)
    eis_df = pd.json_normalize(plot_data)

    try:
        measurements = eis_df['datetime'].unique()
        print(measurements)
    except KeyError:
        print(test)
        print(eis_df)
        continue

    for date in measurements:
        print(date)
        try:
            cycle_df = eis_df[eis_df['datetime'] == date]
            cycle_df.sort_values(by='#', inplace=True)

            ac_amp = round(cycle_df['ac_amp'].iloc[-1], 2)
            print(ac_amp)

            name = str(test) + '_' +  str(date) + '_' + str(ac_amp)

            z_real = cycle_df['z_real'] * 1000 * 25
            z_imag = cycle_df['z_imag'] * -1000 * 25

            traces.append(
                go.Scatter(x=z_real, y=z_imag, mode="markers", marker=dict(size=10, color=palette[c]),
                           line=dict(color=palette[c]),
                           name=name))
        except ValueError:
            print(test, date)
            pass

        if c > 8:
            c = 0
        else:
            c += 1

fig_data = traces

eis_fig = go.Figure(fig_data).update_layout(
    # TITLE
    title='EIS',
    title_font=dict(size=30, color='black'),
    title_x=0.5,
    legend_font=dict(size=16),
    legend=dict(
        x=1.2,
        y=1,
        xanchor='right',  # Set the x anchor to 'right'
        yanchor='top',  # Set the y anchor to 'top'
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
    ),
    plot_bgcolor='white',
)
eis_fig.update_xaxes(title='real [mOhm*cm²]',
                     title_font=dict(size=24, color='black'),
                     tickfont=dict(size=20, color='black'),
                     minor=dict(ticks="inside", ticklen=5, showgrid=False),
                     gridcolor='lightgrey',
                     griddash='dash',
                     showline=True,
                     zeroline=True,
                     zerolinewidth=2,
                     zerolinecolor='black',
                     ticks='inside',
                     ticklen=10,
                     tickwidth=2,
                     linewidth=2,
                     linecolor='black',
                     mirror=True,

                     # range=[0, 650]

                     )
# YAXIS
eis_fig.update_yaxes(title='-imag. [mOhm*cm²]',
                     title_font=dict(size=24, color='black'),
                     tickfont=dict(size=20, color='black'),
                     gridcolor='lightgrey',
                     griddash='dash',
                     minor=dict(ticks="inside", ticklen=5, showgrid=False),
                     showline=True,
                     zeroline=True,
                     zerolinewidth=2,
                     zerolinecolor='black',
                     ticks='inside',
                     ticklen=10,
                     tickwidth=2,
                     linewidth=2,
                     linecolor='black',
                     mirror=True,

                     # range=[-20, 250]
                     )

eis_fig.write_html(
    r'W:\Projekte\#Projektvorbereitung\09-ZBT\Insitu Corrosion\Ergebnisse\operando_analysis\AST_Plots\EIS' + '\\' + 'all_eis' + '.html')

print('plotting successfull!')

eis_fig.show()