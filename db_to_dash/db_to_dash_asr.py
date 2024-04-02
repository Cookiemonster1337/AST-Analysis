from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_asr= sorted([t for t in test_list if t.endswith('EIS')])

palette = px.colors.qualitative.Bold

def plot_asr(test):

    collection = db[test]
    query= {'Hz': {'$lt': 30000}}
    projection = {'datetime': 1, 's':1, 'ac_amp':1, 'z_real': 1, 'z_imag': 1}

    cursor = collection.find(query, projection)

    plot_data = list(cursor)
    asr_df = pd.json_normalize(plot_data)

    asr_df.sort_values(by='datetime', ascending=True)

    print(asr_df.head())



    traces = []
    c = 0

    measurements = asr_df['datetime'].unique()
    print(measurements)

    cycle = 1
    asrs = {}
    cycle_dict = {}
    prev_amp = 5
    for measurement in measurements:
        meas_df = asr_df[asr_df['datetime'] == measurement]

        amp = round(meas_df['ac_amp'].iloc[-1], 2)
        print(amp, prev_amp)
        if amp == prev_amp:
            continue

        imag_up = meas_df[meas_df['z_imag'] > 0]['z_imag'].min()
        real_up = meas_df[meas_df['z_imag'] == imag_up]['z_real'].min()

        # asrs.append(real_up * 1000 * 25)
        asr = real_up * 1000 * 25
        print(amp, asr)


        if amp < prev_amp:
            pass
        else:
            asrs[str(cycle)] = cycle_dict
            cycle_dict = {}
            cycle +=1
            print('cycle: ' + str(cycle))

        cycle_dict[str(amp)] = asr



        prev_amp = round(meas_df['ac_amp'].iloc[-1], 2)

        print(prev_amp)
    asrs[str(cycle)] = cycle_dict
    print(asrs)

    for key, value in asrs.items():
        js = []
        asr = []
        for key2, value2 in value.items():
            j = float(key2)*20/25
            if j%1 != 0:
                js.append(j)
                asr.append(value2)
        traces.append(
            go.Scatter(x=js, y=asr, mode="markers+lines", line=dict(dash='dash'), marker=dict(size=10, color=palette[c]),
                       name=str(key)
                       )
        )
        c += 1
        if c > 8:
            c = 0
        # print(amp)
        # amp_df = asr_df[asr_df['ac_amp'] == amp]
        #
        # print(amp_df)
        #
        #
        #
        # asrs = []
        # for measurement in measurements:
        #     print(measurement)
        #     meas_df = amp_df[amp_df['datetime'] == measurement]
        #
        #     imag_up = meas_df[meas_df['z_imag'] > 0]['z_imag'].min()
        #     real_up = meas_df[meas_df['z_imag'] == imag_up]['z_real'].min()
        #
        #     # name = str(meas_df['datetime'][0])
        #
        #     asrs.append(real_up)
        #
        # # traces.append(
        # #     go.Scatter(x=[amp], y=asrs,
        # #            # text=str(round(current_mean, 3) * 1000) + 'mA<br>' + str(
        # #            #     round(u_perc * 100, 1)) + '%</br>AST-C#' + str(cycle),
        # #            # textposition='auto',
        # #            # textangle=0,
        # #            # insidetextanchor='middle',
        # #            # textfont=dict(size=20, color='black'),
        # #            # marker=dict(size=10, color=palette[c]),
        # #            # error_y=dict(type='data', array=[current_std]),
        # #            name=name
        # #            )
        # # )
        #
        # traces.append(
        #     go.Scatter(x=[amp], y=asrs, mode="markers+lines", marker=dict(size=10, color=palette[c]),
        #                name= str(measurement)
        #                )
        # )
        #
        # c +=1
        #
        # if c>8:
        #     c = 0


    fig_data = traces

    asr_fig = go.Figure(fig_data).update_layout(

        title='ASR ' + '(' + str(test) + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

        xaxis=dict(title='current density [A/cm2]',
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

        yaxis=dict(title='area specific resistance [mohm*cm2]',
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

    asr_fig.write_html(
        r'W:\Projekte\#Projektvorbereitung\09-ZBT\Insitu Corrosion\Ergebnisse\operando_analysis\AST_Plots\ASR' + '\\' + str(
            test) + '.html')

    return asr_fig












