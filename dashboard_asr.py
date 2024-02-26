from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from data_to_graph import drawFigureASRNyquist, drawFigureASRBar, drawFigureASRextrapolation, drawFigureCTRextrapolation
import os

app = Dash(__name__)

app = Dash()

data_folder = 'data'
files = [f for f in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, f))]

app.layout = dbc.Container([

    html.Label("Select file:"),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': file, 'value': file} for file in files],
        value=files[0],
        multi=False
    ),

    # dbc.Row([
    #     dcc.Graph(id='graph-asr-nq', style={'height': '800px'}),
    # ]),
    #
    # # ASR-PLOT
    # dbc.Row([
    #         dcc.Graph(id='graph-asr-bar', style={'height': '800px'}),
    # ]),

    # ASR-PLOT
    dbc.Row([
        dcc.Graph(id='graph-asr-extrapolation', style={'height': '800px'}),
    ]),

    # ASR-PLOT
    dbc.Row([
        dcc.Graph(id='graph-ctr-extrapolation', style={'height': '800px'}),
    ]),



])

@app.callback(
    # Output('graph-asr-nq', 'figure'),
    # Output('graph-asr-bar', 'figure'),
    Output('graph-asr-extrapolation', 'figure'),
    Output('graph-ctr-extrapolation', 'figure'),
    [Input('file-dropdown', 'value')]
)


def update_graph(selected_file):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return drawFigureASRextrapolation(selected_file), drawFigureCTRextrapolation(selected_file)
            # drawFigureASRNyquist(selected_file), \
            #     drawFigureASRBar(selected_file), \



app.run_server(debug=True, port=8084)