import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
import numpy as np

palette = px.colors.qualitative.Bold

def drawFigureTestbench(sample):

    file = r'data' + '\\' + sample + '\summary_60s.csv'

    palette = px.colors.qualitative.Alphabet

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    # test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

    test_data_df['duration/h'] = test_data_df.index * (1 / 60)
    time = test_data_df['duration/h']

    # read in values of interest for plotting from dataframe
    # time = test_data_df['Time Stamp']
    voltage = test_data_df['voltage']
    current = test_data_df['current']

    compression = test_data_df['pressure_stack_compression']

    # CELL
    temp_cell_an = test_data_df['temp_anode_endplate']
    temp_cell_cat = test_data_df['temp_cathode_endplate']

    # COOLANT
    temp_coolant_inlet = test_data_df['temp_coolant_inlet']
    temp_coolant_outlet = test_data_df['temp_coolant_outlet']
    temp_coolant_diff = test_data_df['temp_coolant_in_out_diff']
    pressure_coolant_inlet = test_data_df['pressure_coolant_inlet']
    pressure_coolant_outlet = test_data_df['pressure_coolant_outlet']
    pressure_coolant_diff = test_data_df['pressure_coolant_in_out_diff']

    # ANODE
    temp_an_inlet = test_data_df['temp_anode_inlet']
    temp_an_outlet = test_data_df['temp_anode_outlet']
    temp_an_diff = test_data_df['temp_anode_in_out_diff']
    flow_an = test_data_df['total_anode_stack_flow']
    pressure_an_inlet = test_data_df['pressure_anode_inlet']
    pressure_an_outlet = test_data_df['pressure_anode_outlet']
    pressure_an_diff = test_data_df['pressure_anode_in_out_diff']

    # CATHODE
    temp_cat_inlet = test_data_df['temp_cathode_inlet']
    temp_cat_outlet = test_data_df['temp_cathode_outlet']
    temp_cat_diff = test_data_df['temp_cathode_in_out_diff']
    flow_cat = test_data_df['total_cathode_stack_flow']
    pressure_cat_inlet = test_data_df['pressure_cathode_inlet']
    pressure_cat_outlet = test_data_df['pressure_cathode_outlet']
    pressure_cat_diff = test_data_df['pressure_cathode_in_out_diff']

    # VARIABLES
    var01 = test_data_df['variable_01']
    var02 = test_data_df['variable_02']
    var03 = test_data_df['variable_03']
    var04 = test_data_df['variable_04']
    var05 = test_data_df['variable_05']
    var06 = test_data_df['variable_06']
    var07 = test_data_df['variable_07']
    var08 = test_data_df['variable_08']

    # create traces from values for plot
    fig_overview = make_subplots(specs=[[{"secondary_y": True}]])

    traces_y1 = []
    traces_y2 = []

    # GENERAL
    traces_y1.append(
        go.Scatter(x=time, y=voltage, mode="lines",
                   name='Cell Voltage [Y1]',
                   line=dict(color=palette[0]),
                   yaxis='y1',
                   visible=True
                   )

    )

    traces_y2.append(
        go.Scatter(x=time, y=current, mode="lines",
                   name='Current [Y2]',
                   line=dict(color=palette[1]),
                   yaxis='y2',
                   visible=True
                   )
    )

    # CELL
    traces_y2.append(
        go.Scatter(x=time, y=temp_cell_cat, mode="lines",
                   name='Cell Temperature (Cathode) [Y2]',
                   line=dict(color=palette[16]),
                   yaxis='y2',
                   visible=True
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=temp_cell_an, mode="lines",
                   name='Cell Temperature (Anode) [Y2]',
                   line=dict(color=palette[17]), yaxis='y2',
                   visible='legendonly'
                   )
    )

    # COOLANT
    traces_y1.append(
        go.Scatter(x=time, y=temp_coolant_inlet,
                   mode="lines",
                   name='Temperature Coolant Inlet [Y2]',
                   line=dict(color=palette[16]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_coolant_outlet,
                   mode="lines",
                   name='Temperature Coolant Outlet [Y2]',
                   line=dict(color=palette[17]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_coolant_diff,
                   mode="lines",
                   name='Temperature Coolant Diff [Y1]',
                   line=dict(color=palette[18]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=pressure_coolant_inlet,
                   mode="lines",
                   name='Pressure Coolant Inlet [Y2]',
                   line=dict(color=palette[19]),
                   yaxis='y2',
                   visible='legendonly')
    )

    traces_y1.append(
        go.Scatter(x=time, y=pressure_coolant_outlet,
                   mode="lines",
                   name='Pressure Coolant Outlet [Y2]',
                   line=dict(color=palette[20]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=pressure_coolant_diff,
                   mode="lines",
                   name='Pressure Coolant Diff [Y1]',
                   line=dict(color=palette[21]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    # ANODE
    traces_y1.append(
        go.Scatter(x=time, y=flow_an, mode="lines",
                   name='Flowrate Anode [Y1]',
                   line=dict(color=palette[2]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_an_inlet, mode="lines",
                   name='Temp Anode Inlet [Y2]',
                   line=dict(color=palette[3]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_an_outlet, mode="lines",
                   name='Temp Anode Outlet [Y2]',
                   line=dict(color=palette[4]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_an_diff, mode="lines",
                   name='Temp Anode Diff. [Y2]',
                   line=dict(color=palette[5]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_an_inlet, mode="lines",
                   name='Pressure Anode Inlet [Y2]',
                   line=dict(color=palette[6]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_an_outlet, mode="lines",
                   name='Pressure Anode Outlet [Y2]',
                   line=dict(color=palette[7]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_an_diff, mode="lines",
                   name='Pressure Anode Diff. [Y1]',
                   line=dict(color=palette[8]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    # CATHODE
    traces_y1.append(
        go.Scatter(x=time, y=flow_cat, mode="lines",
                   name='Flowrate Cathode [Y1]',
                   line=dict(color=palette[9]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_cat_inlet, mode="lines",
                   name='Temp Cathode Inlet [Y2]',
                   line=dict(color=palette[10]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_cat_outlet, mode="lines",
                   name='Temp Cathode Outlet [Y2]',
                   line=dict(color=palette[11]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_cat_diff, mode="lines",
                   name='Temp Cathode Diff. [Y2]',
                   line=dict(color=palette[12]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat_inlet, mode="lines",
                   name='Pressure Cathode Inlet [Y2]',
                   line=dict(color=palette[13]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat_outlet, mode="lines",
                   name='Pressure Cathode Outlet [Y2]',
                   line=dict(color=palette[14]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat_diff, mode="lines",
                   name='Pressure Cathode Diff. [Y1]',
                   line=dict(color=palette[15]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    # VARIABLES
    traces_y2.append(
        go.Scatter(x=time, y=var01, mode="lines",
                   name='Load Cycle Count [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var02, mode="lines",
                   name='AST Cycle Count Pt.1 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var03, mode="lines",
                   name='CHAR Cycle Count Pt.1 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var04, mode="lines",
                   name='AST Cycle Count Pt.2 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var08, mode="lines",
                   name='CHAR Cycle Count Pt.2 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    # gather traces in a list which is given to dash-layout-function (drawTestFigureRig)
    traces = traces_y1 + traces_y2

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(

        title='Testbench Parameter (' + sample + ')',
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

    return figure

def drawFigurePOL(sample):

    file = r'data' + '\\' + sample + '\pol.csv'

    palette = px.colors.qualitative.Bold

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)
    test_data_df['current rounded'] = round(test_data_df['current'], 2)

    char_cycles = test_data_df['variable_20'].unique()

    traces = []

    c = 0
    for i in char_cycles:

        cycle_df = test_data_df[test_data_df['variable_20'] == i].reset_index(drop=True)

        currents = cycle_df['current_set'].unique()

        u = []
        j = []
        erry = []

        print(i, currents)

        for current in currents:
            print(len(cycle_df[cycle_df['current_set'] == current]['voltage']))
            j.append(current / 25)
            if current == 0:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'][0:59].mean())
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'][0:59].std())
            if current < 3 and current != 0:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'][60:120].mean())
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'][60:120].std())
            if current > 3 :
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'][240:300].mean())
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'][240:300].std())



        ast_cycle = cycle_df['variable_01'][0]
        load_cycles = cycle_df['variable_02'][0] * (ast_cycle - 1)

        name = '@ ' + str(load_cycles)[:-2] + ' Load Cycles'

        traces.append(
            go.Scatter(x=j, y=u, mode="markers+lines", marker=dict(size=10, color=palette[c]), error_y=dict(array=erry),
                       name=name)
        )

        if c > 5:
            c = 0
        c += 1

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
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

    return figure

def drawFigurePOLDec(sample):

    file = r'data' + '\\' + sample + '\pol.csv'

    palette = px.colors.qualitative.Bold

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

    mask = ()

    test_data_df = test_data_df[
        # test_data_df['File Mark'].str.contains('polcurve_inc', na=False)
        # |
        test_data_df['File Mark'].str.contains('polcurve_dec', na=False)
        ]

    test_data_df['current rounded'] = round(test_data_df['current'], 2)

    char_cycles = test_data_df['variable_20'].unique()

    traces = []

    c = 0
    for i in char_cycles:

        cycle_df = test_data_df[test_data_df['variable_20'] == i].reset_index(drop=True)

        currents = cycle_df['current_set'].unique()

        u = []
        j = []
        erry = []

        for current in currents:
            if current < 46:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).mean())
                j.append(current / 25)
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).std())

        name = cycle_df['Time Stamp'][0]

        traces.append(
            go.Scatter(x=j, y=u, mode="markers+lines", marker=dict(size=10, color=palette[c]), error_y=dict(array=erry),
                       name=name, )
        )
        c += 1

    # AVERAGE POL

    currents = test_data_df['current_set'].unique()

    u = []
    j = []
    erry = []
    errx = []

    for current in currents:
        if current < 46:
            u.append(test_data_df[test_data_df['current_set'] == current]['voltage'].mean())
            j.append(current / 25)
            erry.append(test_data_df[test_data_df['current_set'] == current]['voltage'].std())
            errx.append(0)
    #
    # u.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).mean())
    # j.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).mean() / 25)
    # erry.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).std())
    # errx.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).std() / 25)

    traces.append(
        go.Scatter(x=j, y=u, mode="markers+lines",
                   marker=dict(size=10, color='black'),
                   error_y=dict(array=erry, thickness=1),
                   error_x=dict(array=errx, thickness=1),
                   name='POL Average')
    )

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='POL (decreasing j)',
        title_font=dict(size=30, color='black'),
        title_x=0.4,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

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
                   range=[0, 2]),

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
                   range=[0, 1.2]),

        # LEGEND
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

        # # ANNOTATIONS
        # annotations=[
        #     {
        #         'x': 1.5,  # x-coordinate of the textbox
        #         'y': 1,  # y-coordinate of the textbox
        #         'xref': 'x',
        #         'yref': 'y',
        #         'text': '''
        #         Temperature:\t80°C
        #         <br>rH (Anode):\t50%
        #         <br>rh (Cathode):\t30%
        #         <br>Flow (H2):\t2l/min
        #         <br>Flow (Air):\t 2S
        #         ''',
        #         'bgcolor': 'lightgray'
        #     }
        # ],

        plot_bgcolor='white',
    )
    return figure

def drawFigurePOLInc():

    file = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\kcs#01_pol.csv'

    palette = px.colors.qualitative.Bold

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

    test_data_df = test_data_df[
        test_data_df['File Mark'].str.contains('polcurve_inc', na=False)
        # |
        # test_data_df['File Mark'].str.contains('polcurve_dec', na=False)
        ]

    test_data_df['current rounded'] = round(test_data_df['current'], 2)

    char_cycles = test_data_df['variable_20'].unique()

    traces = []

    c = 0
    for i in char_cycles:

        cycle_df = test_data_df[test_data_df['variable_20'] == i].reset_index(drop=True)

        currents = cycle_df['current_set'].unique()

        u = []
        j = []
        erry = []

        for current in currents:
            if current < 46:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).mean())
                j.append(current / 25)
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).std())

        name = cycle_df['Time Stamp'][0]

        traces.append(
            go.Scatter(x=j, y=u, mode="markers+lines", marker=dict(size=10, color=palette[c]), error_y=dict(array=erry),
                       name=name, )
        )
        c += 1

    # AVERAGE POL

    currents = test_data_df['current_set'].unique()

    u = []
    j = []
    erry = []
    errx = []

    for current in currents:
        if current < 46:
            u.append(test_data_df[test_data_df['current_set'] == current]['voltage'].mean())
            j.append(current / 25)
            erry.append(test_data_df[test_data_df['current_set'] == current]['voltage'].std())
            errx.append(0)
    #
    # u.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).mean())
    # j.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).mean() / 25)
    # erry.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).std())
    # errx.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).std() / 25)

    traces.append(
        go.Scatter(x=j, y=u, mode="markers+lines",
                   marker=dict(size=10, color='black'),
                   error_y=dict(array=erry, thickness=1),
                   error_x=dict(array=errx, thickness=1),
                   name='POL Average')
    )

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='POL (increasing j)',
        title_font=dict(size=30, color='black'),
        title_x=0.4,
        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',
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
                   range=[0, 2]),

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
                   range=[0, 1.2]),

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
    return figure

def drawFigureASRBar(sample):

    file_asr = r'data' + '\\' + sample + '\hfr.csv'

    palette = px.colors.qualitative.Bold

    fig = go.Figure()

    # DATAFRAMES
    try:
        data_df_asr = pd.read_csv(file_asr, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_asr = data_df_asr.sort_values(by=['date', 'time', 'amp'], ascending=[True, True, False])

    count = sorted(data_df_asr['#'].unique())
    print(count)

    c = 0
    for i in count:
        cycle_df_asr = data_df_asr[data_df_asr['#'] == i].reset_index(drop=True)

        current_density = cycle_df_asr['amp'][0]
        date = cycle_df_asr['date'][0]
        time = cycle_df_asr['time'][0]
        char = cycle_df_asr['char'][0]


        f_low = 1E+3
        f_high = 1E+4

        cycle_df_asr = cycle_df_asr[(cycle_df_asr['Hz']> f_low) & (cycle_df_asr['Hz'] < f_high)]
        cycle_df_asr = cycle_df_asr[cycle_df_asr['ohm.1'] < 0]

        asr = cycle_df_asr[cycle_df_asr['ohm.1'] == min(cycle_df_asr['ohm.1'])]['ohm'].iloc[0] * 1000 * 25
        print(asr)

        z_real_asr = cycle_df_asr['ohm'] * 1000 * 25
        z_imag_asr = cycle_df_asr['ohm.1'] * -1000 * 25

        name_asr = str(char) + ' ' + str(date) + ' ' + str(time) + str(current_density) + ' [A/cm²]' + ' ASR ~' + str(round(asr,0)) +' [mOhm*cm²]'

        fig.add_trace(go.Bar(x=[i], y=[asr], marker=dict(color=palette[c]), name=name_asr))

        # cycle_df_asr_sorted = cycle_df_asr.sort_values(by='ohm')
        #
        # # Fit spline
        # print(cycle_df_asr_sorted)
        # x_fit = np.linspace(cycle_df_asr_sorted['ohm'].min(), cycle_df_asr_sorted['ohm'].max(), 100)
        # spline = make_interp_spline(cycle_df_asr_sorted['ohm'], cycle_df_asr_sorted['ohm.1'])
        # y_new = spline(x_fit)
        #
        # x_fit = x_fit * 1000 * 25
        # y_new = y_new * -1000 * 25
        #
        # fig.add_trace(go.Scatter(x=x_fit, y=y_new, mode="lines", marker=dict(size=10, color=palette[c]),
        #                          name=name_asr + ' spline'))

        c += 1
        if c > 10:
            c = 0

    fig.update_layout(
        # TITLE
        title='ASR (' + sample + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
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
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

    return fig

def drawFigureASRNyquist(sample):

    file_asr = r'data' + '\\' + sample + '\hfr.csv'

    palette = px.colors.qualitative.Bold

    # DATAFRAMES
    try:
        data_df_asr = pd.read_csv(file_asr, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_asr = data_df_asr.sort_values(by=['date', 'time', 'amp'], ascending=[True, True, False])

    chars = sorted(data_df_asr['char'].unique())

    color = 0
    traces = []

    for char in chars:
        count = sorted(data_df_asr[data_df_asr['char'] == char]['#'].unique())
        amp = []
        asr = []
        name_asr = str(char)

        for i in count:
            cycle_df_asr = data_df_asr[data_df_asr['#'] == i].reset_index(drop=True)

            amp.append(cycle_df_asr['amp'][0])

            f_low = 1E+3
            f_high = 1E+4

            cycle_df_asr = cycle_df_asr[(cycle_df_asr['Hz']> f_low) & (cycle_df_asr['Hz'] < f_high)]
            cycle_df_asr = cycle_df_asr[cycle_df_asr['ohm.1'] < 0]

            asr.append(cycle_df_asr[cycle_df_asr['ohm.1'] == min(cycle_df_asr['ohm.1'])]['ohm'].iloc[0] * 1000 * 25)
            print(asr)

        traces.append(
            go.Scatter(x=amp, y=asr, mode="markers+lines", marker=dict(size=10, color=palette[color]),
                       name=name_asr)
        )

        color += 1
        if color > 10:
            color = 0

    fig_data = traces

    fig = go.Figure(fig_data).update_layout(
            # TITLE
            title='ASR (' + sample + ')',
            title_font=dict(size=30, color='black'),
            title_x=0.5,
            legend_font = dict(size=16),
            legend = dict(
                x=1.2,
                y=1,
                xanchor='right',  # Set the x anchor to 'right'
                yanchor='top',  # Set the y anchor to 'top'
                bgcolor="white",
                bordercolor="black",
                borderwidth=1,
        ),

        xaxis=dict(title='real [mOhm*cm²]',
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

                       ),
            # YAXIS
        yaxis = dict(title='-imag. [mOhm*cm²]',
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
                       ),
        plot_bgcolor = 'white',
        )

    return fig

def drawFigureASRextrapolation(sample):

    file_asr = r'data' + '\\' + sample + '\hfr.csv'

    # DATAFRAMES
    try:
        data_df_asr = pd.read_csv(file_asr, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_asr = data_df_asr.sort_values(by=['date', 'time', 'amp'], ascending=[True, True, False])

    count = sorted(data_df_asr['#'].unique())

    c = 0
    char = 1
    j = 5

    traces = []


    for i in count:
        cycle_df_asr = data_df_asr[data_df_asr['#'] == i].reset_index(drop=True)

        amp = cycle_df_asr['amp'][0]
        date = cycle_df_asr['date'][0]
        time = cycle_df_asr['time'][0]

        f_low = 1E+2
        f_high = 1E+5

        cycle_df_asr = cycle_df_asr[(cycle_df_asr['Hz']> f_low) & (cycle_df_asr['Hz'] < f_high)]
        # cycle_df_asr = cycle_df_asr[cycle_df_asr['ohm.1'] > -50]

        # Smallest value below zero in each column
        imag_sub = cycle_df_asr[cycle_df_asr['ohm.1'] < 0]['ohm.1'].min()
        real_sub = cycle_df_asr[cycle_df_asr['ohm.1'] == imag_sub]['ohm'].min()

        # Smallest value above zero in each column
        imag_up = cycle_df_asr[cycle_df_asr['ohm.1'] > 0]['ohm.1'].min()
        real_up = cycle_df_asr[cycle_df_asr['ohm.1'] == imag_up]['ohm'].min()

        x = [real_sub, real_up]
        y = [imag_sub, imag_up]
        print(x,y)


        m = (y[1] - y[0]) / (x[1] - x[0])  # slope formula: (y2 - y1) / (x2 - x1)
        b = y[0] - m * x[0]  # y-intercept formula: y1 - m * x1
        x_line = [x[0], x[1]]
        y_line = [m * xi + b for xi in x_line]

        # x_fit = np.linspace(x[0], x[1], 100)
        # spline = make_interp_spline(x, y)
        # y_new = spline(x_fit)

        # asr = cycle_df_asr[cycle_df_asr['ohm.1'] == min(cycle_df_asr['ohm.1'])]['ohm'].iloc[0] * 1000 * 25
        # print(asr)
        #

        asr = round((-b / m) * 1000 * 25, 2)

        name_asr = str(asr)
        #            # str(current_density) + ' [A/cm²]' + ' ASR ~' + str(round(asr,0)) +' [mOhm*cm²]'
        #
        # # fig.add_trace(go.Bar(x=[i], y=[asr], marker=dict(color=palette[c]), name=name_asr))
        #
        # cycle_df_asr = cycle_df_asr.drop_duplicates(subset='ohm', keep=False)
        # cycle_df_asr_sorted = cycle_df_asr.sort_values(by='ohm')
        #
        # x = cycle_df_asr_sorted['ohm'] * 1000 * 25
        # y = cycle_df_asr_sorted['ohm.1'] * 1000 * 25
        #
        # # Fit spline
        # print(cycle_df_asr_sorted)
        # x_fit = np.linspace(x.min()-100, x.max(), 100)
        # spline = make_interp_spline(x, y)
        # y_new = spline(x_fit)

        traces.append(go.Scatter(x=x, y=y, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_asr))

        traces.append(go.Scatter(x=x_line, y=y_line, mode="lines", marker=dict(size=10, color=palette[c])))



        c += 1
        if c > 10:
            c = 0

    fig = go.Figure(traces).update_layout(
        # TITLE
        title='ASR (' + sample + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
        ),
        xaxis = dict(title='real [mOhm*cm²]',
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
        yaxis = dict(title='-imag. [mOhm*cm²]',
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
                       ),
        plot_bgcolor = 'white',
        )
    return fig

def drawFigureCTRextrapolation(sample):

    file_asr = r'data' + '\\' + sample + '\hfr.csv'

    # DATAFRAMES
    try:
        data_df_asr = pd.read_csv(file_asr, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_asr = data_df_asr.sort_values(by=['date', 'time', 'amp'], ascending=[True, True, False])

    count = sorted(data_df_asr['#'].unique())

    c = 0
    char = 1
    j = 5

    traces = []


    for i in count:
        cycle_df= data_df_asr[data_df_asr['#'] == i].reset_index(drop=True)

        z_real = cycle_df['ohm']
        z_imag = cycle_df['ohm.1']

        amp = cycle_df['amp'][0]
        date = cycle_df['date'][0]
        time = cycle_df['time'][0]

        f_low = 1E+2
        f_high = 1E+5

        cycle_df_asr = cycle_df[(cycle_df['Hz']> f_low) & (cycle_df['Hz'] < f_high)]
        # cycle_df_asr = cycle_df_asr[cycle_df_asr['ohm.1'] > -50]

        # Smallest value below zero in each column
        imag_sub = cycle_df_asr[cycle_df_asr['ohm.1'] < 0]['ohm.1'].min()
        real_sub = cycle_df_asr[cycle_df_asr['ohm.1'] == imag_sub]['ohm'].min()

        # Smallest value above zero in each column
        imag_up = cycle_df_asr[cycle_df_asr['ohm.1'] > 0]['ohm.1'].min()
        real_up = cycle_df_asr[cycle_df_asr['ohm.1'] == imag_up]['ohm'].min()



        x = [real_sub, real_up]
        y = [imag_sub, imag_up]
        print(x,y)


        m = (y[1] - y[0]) / (x[1] - x[0])  # slope formula: (y2 - y1) / (x2 - x1)
        b = y[0] - m * x[0]  # y-intercept formula: y1 - m * x1
        x_line = [x[0], x[1]]
        y_line = [m * xi + b for xi in x_line]

        asr = round((-b / m) * 1000 * 25, 2)

        name_asr = str(asr)

        # traces.append(go.Scatter(x=x, y=y, mode="markers", marker=dict(size=10, color=palette[c]),
        #                          name=name_asr))

        traces.append(go.Scatter(x=x_line, y=y_line, mode="lines", marker=dict(size=10, color=palette[c]),
                                 name=name_asr))

        f_low = 1E-1
        f_high = 1E+2


        cycle_df_ctr = cycle_df[(cycle_df['Hz'] > f_low) & (cycle_df['Hz'] < f_high)]

        # Smallest value below zero in each column
        imag_sub = cycle_df_ctr[cycle_df_ctr['ohm.1'] < 0]['ohm.1'].min()
        real_sub = cycle_df_ctr[cycle_df_ctr['ohm.1'] == imag_sub]['ohm'].min()

        # Smallest value above zero in each column
        imag_up = cycle_df_ctr[cycle_df_ctr['ohm.1'] > 0]['ohm.1'].min()
        real_up = cycle_df_ctr[cycle_df_ctr['ohm.1'] == imag_up]['ohm'].min()

        x = [real_sub, real_up]
        y = [imag_sub, imag_up]
        print(x, y)

        m = (y[1] - y[0]) / (x[1] - x[0])  # slope formula: (y2 - y1) / (x2 - x1)
        b = y[0] - m * x[0]  # y-intercept formula: y1 - m * x1
        x_line = [x[0], x[1]]
        y_line = [m * xi + b for xi in x_line]

        ctr = round((-b / m) * 1000 * 25, 2)
        if np.isnan(x[-1]):
            ctr = round(x[0] * 1000 * 25, 2)

        name_ctr = str(ctr)

        traces.append(go.Scatter(x=z_real, y=z_imag, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_ctr))

        traces.append(go.Scatter(x=x_line, y=y_line, mode="lines", marker=dict(size=10, color=palette[c]),
                                 name=name_ctr))

        c += 1
        if c > 10:
            c = 0

    fig = go.Figure(traces).update_layout(
        # TITLE
        title='ASR (' + sample + ')',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
        ),
        xaxis = dict(title='real [mOhm*cm²]',
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
        yaxis = dict(title='-imag. [mOhm*cm²]',
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
                       ),
        plot_bgcolor = 'white',
        )
    return fig

def drawFigureEIS5a(sample):

    file_5a = r'data' + '\\' + sample + '\eis_5a.csv'

    palette = px.colors.qualitative.Bold

    fig = go.Figure()

    # DATAFRAMES
    try:
        data_df_5a = pd.read_csv(file_5a, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_5a = data_df_5a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_5a['#'].unique())

    c = 0
    for i in count:
        cycle_df_5a = data_df_5a[data_df_5a['#'] == i].reset_index(drop=True)


        name_5a = '#' + str(i) + '_' + cycle_df_5a['date'][0] + ' ' + cycle_df_5a['time'][0]

        z_real_5a = cycle_df_5a['ohm'] * 1000 * 25
        z_imag_5a = cycle_df_5a['ohm.1'] * -1000 * 25

        fig.add_trace(go.Scatter(x=z_real_5a, y=z_imag_5a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_5a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS @0.2A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
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
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
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


    return fig

def drawFigureEIS25a(sample):

    file_25a = r'data' + '\\' + sample + '\eis_25a.csv'

    palette = px.colors.qualitative.Bold

    # create traces from values for plot
    fig = go.Figure()

    # DATAFRAMES
    try:
        data_df_25a = pd.read_csv(file_25a, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_25a = data_df_25a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_25a['#'].unique())

    c = 0
    for i in count:
        cycle_df_25a = data_df_25a[data_df_25a['#'] == i].reset_index(drop=True)

        name_25a = '#' + str(i) + '_' + cycle_df_25a['date'][0] + ' ' + cycle_df_25a['time'][0]

        z_real_25a = cycle_df_25a['ohm'] * 1000 * 25
        z_imag_25a = cycle_df_25a['ohm.1'] * -1000 * 25

        fig.add_trace(go.Scatter(x=z_real_25a, y=z_imag_25a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_25a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS (Nyquist) @1A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
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
                   #
                   # range=[0, 180]

                    )

        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

                   # range=[0, 120]
                   )
    return fig

def drawFigureEIS50a(sample):

    file_50a = r'data' + '\\' + sample + '\eis_50a.csv'

    palette = px.colors.qualitative.Bold

    fig = go.Figure()

    # DATAFRAMES
    try:
        data_df_50a = pd.read_csv(file_50a, encoding='cp1252', low_memory=False)
    except:
        textbox_annotation = {
            'x': 0.5,
            'y': 0.5,
            'xref': 'paper',
            'yref': 'paper',
            'text': 'No Data!',
            'showarrow': False,
            'font': {'size': 40, 'color': 'red'}
        }

        fig.update_layout(
            # TITLE
            title='EIS (Nyquist) @2A/cm²',
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
            annotations=[textbox_annotation]
        )
        fig.update_xaxes(title='real [mOhm*cm²]',
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
                         #
                         # range=[0, 1000]
                         )
        # YAXIS
        fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

                         # range=[-20, 600]
                         )

        return fig

    data_df_50a = data_df_50a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_50a['#'].unique())

    c = 0
    for i in count:
        cycle_df_50a = data_df_50a[data_df_50a['#'] == i].reset_index(drop=True)


        name_50a = '#' + str(i) + '_' + cycle_df_50a['date'][0] + ' ' + cycle_df_50a['time'][0]

        z_real_50a = cycle_df_50a['ohm'] * 1000 * 25
        z_imag_50a = cycle_df_50a['ohm.1'] * -1000 * 25

        fig.add_trace(go.Scatter(x=z_real_50a, y=z_imag_50a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_50a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS (Nyquist) @2A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
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
                     #
                     # range=[0, 1000]
                     )
        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

                   # range=[-20, 600]
                   )


    return fig

def drawFigureEIS75a(sample):

    file_75a = r'data' + '\\' + sample + '\eis_75a.csv'

    palette = px.colors.qualitative.Bold

    fig = go.Figure()

    # DATAFRAMES
    try:
        data_df_75a = pd.read_csv(file_75a, encoding='cp1252', low_memory=False)
        print('data')
    except:
        textbox_annotation = {
            'x': 0.5,
            'y': 0.5,
            'xref': 'paper',
            'yref': 'paper',
            'text': 'No Data!',
            'showarrow': False,
            'font': {'size': 40, 'color': 'red'}
        }


        fig.update_layout(
            # TITLE
            title='EIS (Nyquist) @3A/cm²',
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
            annotations=[textbox_annotation]
        )
        fig.update_xaxes(title='real [mOhm*cm²]',
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
                         #
                         # range=[0, 1000]
                         )
        # YAXIS
        fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

                         # range=[-20, 600]
                         )

        return fig

    data_df_75a = data_df_75a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_75a['#'].unique())

    c = 0
    for i in count:
        cycle_df_75a = data_df_75a[data_df_75a['#'] == i].reset_index(drop=True)


        name_75a = '#' + str(i) + '_' + cycle_df_75a['date'][0] + ' ' + cycle_df_75a['time'][0]

        z_real_75a = cycle_df_75a['ohm'] * 1000 * 25
        z_imag_75a = cycle_df_75a['ohm.1'] * -1000 * 25

        fig.add_trace(go.Scatter(x=z_real_75a, y=z_imag_75a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_75a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS (Nyquist) @3A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
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
                     #
                     # range=[0, 1000]
                     )
        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

                   # range=[-20, 600]
                   )


    return fig

def drawFigureEIS100a(sample):

    file_100a = r'data' + '\\' + sample + '\eis_100a.csv'

    palette = px.colors.qualitative.Bold

    # create traces from values for plot
    fig = go.Figure()

    # DATAFRAMES
    try:
        data_df_100a = pd.read_csv(file_100a, encoding='cp1252', low_memory=False)
    except:
        return

    data_df_100a = data_df_100a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_100a['#'].unique())

    c = 0
    for i in count:
        cycle_df_100a = data_df_100a[data_df_100a['#'] == i].reset_index(drop=True)

        name_100a = '#' + str(i) + '_' + cycle_df_100a['date'][0] + ' ' + cycle_df_100a['time'][0]

        z_real_100a = cycle_df_100a['ohm'] * 1000
        z_imag_100a = cycle_df_100a['ohm.1'] * -1000

        fig.add_trace(go.Scatter(x=z_real_100a, y=z_imag_100a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_100a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS (Nyquist) @4A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
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
                   #
                   # range=[0, 180]

                    )

        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
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

                   # range=[0, 120]
                   )
    return fig

def drawFigureCV(sample):

    from plotly.offline import download_plotlyjs, init_notebook_mode, plot
    from plotly.subplots import make_subplots
    import plotly.graph_objs as go
    import pandas as pd
    import plotly.express as px
    import os

    file = r'data' + '\\' + sample + '\cv_0-900_20mVs.csv'

    palette = px.colors.qualitative.Bold

    data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    data_df = data_df.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df['#'].unique())

    traces = []

    c = 0
    for i in count:
        print(i)
        cycle_df = data_df[data_df['#'] == i]
        cycle_df = cycle_df[cycle_df['#.2'] == 5].reset_index(drop=True)

        try:
            name = '#' + str(i) + '_' + cycle_df['date'][0] + ' ' + cycle_df['time'][0]
        except KeyError:
            name = 'x'
            print(cycle_df['date'])

        u = cycle_df['V vs. Ref.'] * 1000
        j = cycle_df['A'] * 1000 / 25

        traces.append(
            go.Scatter(x=u, y=j, mode="lines", marker=dict(size=10, color=palette[c]), line=dict(color=palette[c]),
                       name=name))


        if c > 5:
            c = 0
        else:
            c += 1

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='CV-Analysis (@100 mV/s)',
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
        yaxis=dict(title='current [mA]',
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

    return figure