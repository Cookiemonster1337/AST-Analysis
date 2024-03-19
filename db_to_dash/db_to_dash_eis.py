from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_eis = [t for t in test_list if t.endswith('EIS')]

palette = px.colors.qualitative.Bold

def plot_eis(test):

    collection = db[test]
    query = {'mode':'char'}
    projection = {'#':1, 'z_real':1, 'z_imag':1, 'amp':1, 'datetime':1, 'Hz':1, 'source_file':1}

    cursor = collection.find(query, projection)

    plot_data = list(cursor)
    eis_df = pd.json_normalize(plot_data)

    measurements = eis_df['datetime'].unique()

    traces = []
    c = 0

    for date in measurements:

        cycle_df = eis_df[eis_df['datetime'] == date]
        cycle_df.sort_values(by='#', inplace=True)

        name = str(date)

        z_real = cycle_df['z_real'] * 1000 * 25
        z_imag = cycle_df['z_imag'] * -1000 * 25

        traces.append(
            go.Scatter(x=z_real, y=z_imag, mode="lines", marker=dict(size=10, color=palette[c]), line=dict(color=palette[c]),
                       name=name))

        if c > 5:
            c = 0
        else:
            c += 1

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='EIS @0.2A/cm²',
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
    figure.update_xaxes(title='real [mOhm*cm²]',
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
    figure.update_yaxes(title='-imag. [mOhm*cm²]',
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

    return figure