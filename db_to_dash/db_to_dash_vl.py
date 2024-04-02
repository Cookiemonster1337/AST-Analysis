from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_vl_ast1 = sorted([t for t in test_list if t.endswith('TB') and 'ast01' in t])
test_list_vl_ast2 = sorted([t for t in test_list if t.endswith('TB') and 'ast02' in t])

def plot_vl(test, op):

    # define collection dependent on dropdwon selection
    collection = db[test]

    # define query dependent on used ast protcol
    #todo used protocol to be implemented in testbench entries
    if 'ast01' in str(test):
        if op == '400mv':
            query = {'File Mark':{'$in':['400mV_CYCLE-I']}}
        if op == '600mv':
            query = {'File Mark':{'$in':['600mV_CYCLE-I']}}

    if 'ast02' in str(test):
        if op == '5mv':
            query = {'File Mark': {'$in': ['5mV_CYCLE-I']}}
        if op == '880mv':
            query = {'File Mark': {'$in': ['880mV_CYCLE-I']}}
    else:
        print('query not defined!')
        pass

    # define keys of interest for plot
    projection = {'datetime': 1,
                  'current': 1,
                  'voltage': 1,
                  'variable_01': 1,
                  }

    cursor = collection.find(query, projection)
    print('query data...')

    plot_data = list(cursor)

    vl_df = pd.json_normalize(plot_data)
    print(vl_df.head())
    print('data query successfull')

    vl_df.sort_values(by='datetime', inplace=True)

    char_cycles = vl_df['variable_01'].unique()
    print('CHAR-Cycles: ' + str(len(char_cycles)))
    traces = []

    c = 0
    for i in char_cycles:
        vl_cycle_df = vl_df[vl_df['variable_01'] == i].reset_index(drop=True)
        current_mean = vl_cycle_df['current'].mean()
        current_std = vl_cycle_df['current'].std()

        cycle = int(i)

        name = '#' + str(cycle)

        if cycle == 1:
            current_ref = current_mean

        u_perc = current_mean / current_ref

        traces.append(
            go.Bar(x=[i], y=[current_mean],
                   text=str(round(current_mean, 3) * 1000) + 'mA<br>' + str(round(u_perc *100,1)) + '%</br>AST-C#' + str(cycle),
                   textposition ='auto',
                   textangle= 0,
                   insidetextanchor='middle',
                   textfont=dict(size=20, color='black'),
                   # marker=dict(size=10, color=palette[c]),
                   # error_y=dict(type='data', array=[current_std]),
                   name=name
                   )
        )
    traces_y1 = []
    traces_y2 = []

    fig_data = traces

    vl_fig = go.Figure(fig_data).update_layout(

        title='current_density @' + str(op) + ' (' + str(test) + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

        xaxis=dict(title='AST-Cycle',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   # minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   # gridcolor='lightgrey',
                   # griddash='dash',
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

        yaxis=dict(title='current @' + str(op),
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

    vl_fig.write_html(
        r'W:\Projekte\#Projektvorbereitung\09-ZBT\Insitu Corrosion\Ergebnisse\operando_analysis\AST_Plots\CL' + '\\' + str(test) + '_' + str(op) + '.html')

    return vl_fig