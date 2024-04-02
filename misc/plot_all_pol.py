# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 07:29:33 2024

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
test_list_char = sorted([t for t in test_list if t.endswith('CHAR')])

traces = []
c = 0
for test in test_list_char:
    collection = db[test]
    cycles = collection.distinct('variable_01')

    for cycle in cycles:
        query = {'File Mark': {'$in': ['pol', 'hfr', 'eis']}, 'variable_01': cycle}
        projection = {'datetime': 1,
                      'current': 1,
                      'voltage': 1,
                      'variable_08': 1,
                      'current_set': 1,
                      'variable_02': 1
                      }

        cursor = collection.find(query, projection)
        print('query data...')

        plot_data = list(cursor)

        cycle_df = pd.json_normalize(plot_data)

        name = str(test) + str(cycle)

        currents = cycle_df['current_set'].unique()

        u = []
        j = []
        erry = []

        for current in currents:
            j.append(current / 25)
            if current == 0:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'][0:59].mean())
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'][0:59].std())
            if current < 3 and current != 0:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'][60:120].mean())
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'][60:120].std())
            if current > 3:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'][240:300].mean())
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'][240:300].std())

        traces.append(
            go.Scatter(x=j, y=u, mode="markers+lines", marker=dict(size=10, color=palette[c]), error_y=dict(array=erry),
                       name=name)
        )

        c += 1
        if c > 8:
            c = 0

fig_data = traces

pol_fig = go.Figure(fig_data).update_layout(
    # TITLE
    title='POL-Analysis',
    title_font=dict(size=30, color='black'),
    title_x=0.4,
    # XAXIS
    xaxis=dict(title='current density [A/cm²]',
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
               # range=[0, 2]
               ),

    # YAXIS
    yaxis=dict(title='voltage [V]',
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
               # range=[0, 1.2]
               ),

    legend_font=dict(size=16),
    legend=dict(
        x=1.3,
        y=1,
        xanchor='right',  # Set the x anchor to 'right'
        yanchor='top',  # Set the y anchor to 'top'
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
    ),
    plot_bgcolor='white',
)

pol_fig.write_html(
    r'W:\Projekte\#Projektvorbereitung\09-ZBT\Insitu Corrosion\Ergebnisse\operando_analysis\AST_Plots\POL' + '\\' + 'all_pol' + '.html')

print('plotting successfull!')

pol_fig.show()