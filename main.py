import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dataframes import drawFigureTestbench, drawFigureCV, \
    drawFigureEIS25a, drawFigureEIS50a, drawFigureEIS5a, drawFigureEIS75a, drawFigureEIS100a, drawFigurePOL
import os


app = Dash(__name__)

app = Dash()

data_folder = 'data'
files = [f for f in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, f))]

app.layout = dbc.Container([

        html.Label("Select a file:"),
        dcc.Dropdown(
            id='file-dropdown',
            options=[{'label': file, 'value': file} for file in files],
            value=files[0],
            multi=False
        ),

    # # ROW1 #############################################################################################################
    # dbc.Row([
    #     html.H1('Testbench Parameter Monitoring'),
    #     dcc.Markdown('''
    #     Testbench Paramaeter Monitoring during operation of entire ST-Protocol \n
    #     Including Load Cycling, Shutdown, Startup and electrochemical Cahracterization Procedures
    #     '''),
    # ]),

    # ROW1 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-tb', style={'height': '800px'}),
    ]),

    # ROW2 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-pol', style={'height': '800px'})
    ]),

    # # # ROW3 #############################################################################################################
    # # dbc.Row([
    # #     dcc.Graph(id='graph-pol-inc', figure=drawFigurePOLInc(), style={'height': '800px'})
    # # ]),
    #
    #
    # ROW4 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-eis-5a', style={'height': '800px'}),
    ]),

    # #
    # ROW5 #############################################################################################################
    dbc.Row([
        dcc.Graph(id='graph-eis-25a', style={'height': '800px'}),
    ]),
    #
    # ROW6 #############################################################################################################
    dbc.Row([
        dcc.Graph(id='graph-eis-50a', style={'height': '800px'}),
    ]),
    #
    #
    # ROW6 #############################################################################################################
    dbc.Row([
        dcc.Graph(id='graph-eis-75a', style={'height': '800px'}),
    ]),
    #
    # # ROW6 #############################################################################################################
    # dbc.Row([
    #     dcc.Graph(id='graph-eis-100a', style={'height': '800px'}),
    # ]),
    #
    # ROW7 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-cv', style={'height': '800px'}),
    ]),

    ])

@app.callback(
    Output('graph-tb', 'figure'),
    Output('graph-pol', 'figure'),
    Output('graph-eis-5a', 'figure'),
    Output('graph-eis-25a', 'figure'),
    Output('graph-eis-50a', 'figure'),
    Output('graph-eis-75a', 'figure'),
    Output('graph-cv', 'figure'),
    [Input('file-dropdown', 'value')]
)
def update_graph(selected_file):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return drawFigureTestbench(selected_file), \
            drawFigurePOL(selected_file), \
            drawFigureEIS5a(selected_file), \
            drawFigureEIS25a(selected_file), \
            drawFigureEIS50a(selected_file), \
            drawFigureEIS75a(selected_file), \
            drawFigureCV(selected_file)

app.run_server(debug=True,
               port=8080
               )

