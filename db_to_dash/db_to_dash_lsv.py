from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_cv = [t for t in test_list if t.endswith('CV')]

palette = px.colors.qualitative.Bold

def plot_lsv(test):

    collection = db[test]
    query = {'mode':{'$in': ['lsv_p1', 'lsv_p2']}}
    projection = {'#':1, 's':1, 'A':1, 'v_vs_ref':1, 'datetime':1, 'source_file':1}

    cursor = collection.find(query, projection)

    plot_data = list(cursor)
    cv_df = pd.json_normalize(plot_data)

    cv_df.sort_values(by='datetime', inplace=True)

    measurements = cv_df['datetime'].unique()
    print(measurements)
    traces = []
    c = 0
    i = 1

    for date in measurements[1::2]:
        print(date)

        cycle_df_p1 = cv_df[(cv_df['datetime'] == date)]

        cycle_df_p2 = cv_df[(cv_df['datetime'] == measurements[i + 1])]
        i += 2

        cycle_df_p2['#'] = cycle_df_p2['#'] + cycle_df_p1['#'].max()
        cycle_df_p2['s'] = cycle_df_p2['s'] + cycle_df_p1['s'].max()

        cycle_df_p1.sort_values(by='#', inplace=True)
        cycle_df_p2.sort_values(by='#', inplace=True)

        cycle_df = pd.concat([cycle_df_p1[:-5], cycle_df_p2[5:]])

        cycle_df.sort_values(by='#', inplace=True)

        name = str(str(date)[:-10])

        time = cycle_df['s']
        u = cycle_df['v_vs_ref'] * 1000
        j = cycle_df['A'] * 1000 / 25

        traces.append(
            go.Scatter(x=time, y=j, mode="lines", marker=dict(size=10, color=palette[c]), line=dict(color=palette[c]),
                       name=name, yaxis='y2'))

        traces.append(
            go.Scatter(x=time, y=u, mode="lines", marker=dict(size=10, color=palette[c]), line=dict(color=palette[c]),
                       name=name, yaxis='y1'))

        if c > 5:
            c = 0
        else:
            c += 1

    fig_data = traces

    lsv_fig = go.Figure(fig_data).update_layout(

        title='LSV Analysis (' + str(test) + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

        xaxis=dict(title='time [s]',
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

        yaxis=dict(title='voltage [mV]',
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

        yaxis2=dict(title='current [mA/cm2]',
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

    return lsv_fig