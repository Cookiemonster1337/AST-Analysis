from pymongo import MongoClient
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import time

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_coating_char

collection = db['gts-tb']

query_name = 'ast1_coated_#01'

query = {'test_id': query_name,
}

projection = {'Time Stamp': 1,'current':1, 'voltage':1, 'temp_cathode_endplate':1, 'File Mark':1}

cursor = collection.find(query, projection)

data_list = list(cursor)

df_export = pd.json_normalize(data_list)

client.close()

df_export['duration/h'] = df_export.index * 1 / 3600
duration = df_export['duration/h']

current = df_export['current']
voltage = df_export['voltage']
temp_cell_cat = df_export['temp_cathode_endplate']

print(df_export['File Mark'].unique())

fig_overview = make_subplots(specs=[[{"secondary_y": True}]])

traces_y1 = []
traces_y2 = []

traces_y1.append(
    go.Scatter(x=duration, y=voltage, mode="lines",
               name='Cell Voltage [Y1]',
               line=dict(color='black'), yaxis='y1'))

traces_y2.append(
    go.Scatter(x=duration, y=current, mode="lines",
               name='Current [Y2]',
               line=dict(color='red'), yaxis='y2'))

traces_y2.append(
    go.Scatter(x=duration, y=temp_cell_cat, mode="lines",
               name='Temp. Cell (Cathode) [Y2]',
               line=dict(color='blue'), yaxis='y2'))

traces = traces_y1 + traces_y2

fig_data = traces



fig_test= go.Figure(fig_data).update_layout(
    title='FTC-Testbench Parameter Monitoring',
    title_font=dict(size=30, color='black'),
    title_x=0.3,
    xaxis=dict(title='duration [h]',
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
               ),
    yaxis=dict(title='parameter selecetion',
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
               range=[0, 1.2]
               ),

    yaxis2=dict(title='parameter selection',
                overlaying='y',
                side='right',
                title_font=dict(size=24, color='black'),
                tickfont=dict(size=20, color='black'),
                minor=dict(ticks="inside", ticklen=5, showgrid=False),
                ticks='inside',
                ticklen=10,
                tickwidth=2,

                linewidth=2,
                linecolor='black',
                range=[-10, 120]
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

end_time_plot = time.time()
elapsed_time_plot = end_time_plot - start_time_plot
print(elapsed_time_plot)

fig_test.show()

