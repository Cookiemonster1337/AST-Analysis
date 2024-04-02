from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_tb = sorted([t for t in test_list if t.endswith('TB')])

def plot_tb(test):

    collection = db[test]
    query = {}
    projection = {'datetime': 1,
                  'current': 1,
                  'voltage': 1,
                  # 'pressure_anode_inlet' : 1,
                  # 'pressure_cathode_inlet' : 1,
                  # 'temp_cathode_endplate': 1,
                  # 'temp_anode_endplate': 1,
                  # 'total_anode_stack_flow': 1,
                  # 'total_cathode_stack_flow': 1,
                  # 'temp_anode_inlet': 1,
                  # 'temp_cathode_inlet': 1,
                  # 'temp_anode_dewpoint_water': 1,
                  # 'temp_cathode_dewpoint_water': 1,
                  }

    cursor = collection.find(query, projection)

    plot_data = list(cursor)
    tb_df = pd.json_normalize(plot_data)

    tb_df.sort_values(by='datetime', inplace=True)

    tb_df['duration/h'] = tb_df.index * 1 / 3600
    # duration = tb_df['duration/h']
    duration = tb_df['datetime']
    current = tb_df['current']
    voltage = tb_df['voltage']
    # flow_an_inlet = tb_df['total_anode_stack_flow']
    # flow_cat_inlet = tb_df['total_cathode_stack_flow']
    # pressure_an_inlet= tb_df['pressure_anode_inlet']
    # pressure_cat_inlet = tb_df['pressure_cathode_inlet']
    # temp_cell_cat = tb_df['temp_cathode_endplate']
    # temp_cell_an = tb_df['temp_anode_endplate']
    # temp_an_inlet = tb_df['temp_anode_inlet']
    # temp_cat_inlet = tb_df['temp_cathode_inlet']
    # temp_an_hum = tb_df['temp_anode_dewpoint_water']
    # temp_cat_hum = tb_df['temp_cathode_dewpoint_water']

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

    # traces_y2.append(
    #     go.Scatter(x=duration, y=flow_an_inlet, mode="lines",
    #                name='Gas Flow (A) [Y2]',
    #                line=dict(color='lightblue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=flow_cat_inlet, mode="lines",
    #                name='Gas Flow (C) [Y2]',
    #                line=dict(color='blue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=pressure_an_inlet, mode="lines",
    #                name='Pressure Inlet (A) [Y2]',
    #                line=dict(color='lightblue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=pressure_cat_inlet, mode="lines",
    #                name='Pressure Inlet (C) [Y2]',
    #                line=dict(color='blue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=temp_an_inlet, mode="lines",
    #                name='Temp. Cell (A) [Y2]',
    #                line=dict(color='lightblue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=temp_cell_cat, mode="lines",
    #                name='Temp. Cell (C) [Y2]',
    #                line=dict(color='blue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=temp_cell_an, mode="lines",
    #                name='Temp. Cell (Anode) [Y2]',
    #                line=dict(color='lightblue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=temp_cat_inlet, mode="lines",
    #                name='Temp. Gas (C) [Y2]',
    #                line=dict(color='blue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=flow_an_inlet, mode="lines",
    #                name='Gas Flow (A) [Y2]',
    #                line=dict(color='lightblue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=flow_cat_inlet, mode="lines",
    #                name='Gas Flow (C) [Y2]',
    #                line=dict(color='blue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=temp_an_hum, mode="lines",
    #                name='Temp. Hum. (A) [Y2]',
    #                line=dict(color='lightblue'), yaxis='y2'))
    #
    # traces_y2.append(
    #     go.Scatter(x=duration, y=temp_cat_hum, mode="lines",
    #                name='Temp. Hum. (C) [Y2]',
    #                line=dict(color='blue'), yaxis='y2'))

    traces = traces_y1 + traces_y2

    fig_data = traces

    tb_fig = go.Figure(fig_data).update_layout(

        title='Testbench Parameter (' + str(test) + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

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

        yaxis=dict(title='arbitrary unit [Y1]',
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
                   range=[0, 1.2]),

        yaxis2=dict(title='arbitrary unit [Y2]',
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

    tb_fig.write_html(
        r'W:\Projekte\#Projektvorbereitung\09-ZBT\Insitu Corrosion\Ergebnisse\operando_analysis\AST_Plots\TB' + '\\' + str(test) + '.html')

    return tb_fig