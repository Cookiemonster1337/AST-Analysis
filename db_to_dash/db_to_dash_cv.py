from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_cv = sorted([t for t in test_list if t.endswith('CV')])

palette = px.colors.qualitative.Bold

def plot_cv(test):

    collection = db[test]
    query = {'mode':'cv'}
    projection = {'#':1, 'A':1, 'v_vs_ref':1, 'datetime':1, 'source_file':1}

    cursor = collection.find(query, projection)

    plot_data = list(cursor)
    cv_df = pd.json_normalize(plot_data)

    measurements = cv_df['datetime'].unique()

    traces = []
    c = 0

    for date in measurements:

        cycle_df = cv_df[cv_df['datetime'] == date]
        cycle_df.sort_values(by='#', inplace=True)
        cycle_df = cycle_df[-2000:]

        name = str(date)

        u = cycle_df['v_vs_ref'] * 1000
        j = cycle_df['A'] * 1000 / 25

        traces.append(
            go.Scatter(x=u, y=j, mode="lines", marker=dict(size=10, color=palette[c]), line=dict(color=palette[c]),
                       name=name))

        if c > 5:
            c = 0
        else:
            c += 1

    fig_data = traces

    cv_fig = go.Figure(fig_data).update_layout(
        # TITLE
        title='CV-Analysis (' + str(test) + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        # XAXIS
        xaxis=dict(title='voltage [mV]',
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

                   range=[0, -1000],
                   # autorange='reversed',
                   ),

        # YAXIS
        yaxis=dict(title='current [mA/cm2]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='darkgrey',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   autorange='reversed'
                   ),

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

    cv_fig.write_html(
        r'W:\Projekte\#Projektvorbereitung\09-ZBT\Insitu Corrosion\Ergebnisse\operando_analysis\AST_Plots\CV' + '\\'  + str(test) + '.html')

    print('plotting successfull!')


    return cv_fig