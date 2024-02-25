from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from data_to_graph import drawFigureTestbench
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

    # TB-PLOT
    dbc.Row([
        dcc.Graph(id='graph-tb', style={'height': '800px'}),
    ]),

])

@app.callback(
    Output('graph-tb', 'figure'),
    [Input('file-dropdown', 'value')]
)


def update_graph(selected_file):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return drawFigureTestbench(selected_file)


app.run_server(debug=True, port=8080)