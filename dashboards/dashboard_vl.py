from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from db_to_dash.db_to_dash_pol import test_list_tb, plot_pol

app = Dash(__name__)

app = Dash()

app.layout = dbc.Container([

    html.Label("Select file:"),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': test, 'value': test} for test in test_list_tb],
        value=test_list_tb[0],
        multi=False
    ),

    # TB-PLOT
    dbc.Row([
        dcc.Graph(id='graph-pol', style={'height': '800px'}),
    ]),

])