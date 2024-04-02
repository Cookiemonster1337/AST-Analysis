from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from db_to_dash.db_to_dash_vl import test_list_vl_ast2, plot_vl

app = Dash(__name__)

app.title = 'AST2-CL'

app.layout = dbc.Container([

    html.Label("Select file:"),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': test, 'value': test} for test in test_list_vl_ast2],
        value=test_list_vl_ast2[0],
        multi=False
    ),



    dbc.Row(dcc.Tabs(id='tabs-vl', value='5mv', children=[
        # dcc.Tab(label='OCV', value='ocv'),
        dcc.Tab(label='5 mV', value='5mv'),
        dcc.Tab(label='880 mV', value='880mv'),
    ])),

    # VL-PLOT
    dbc.Row([
        dcc.Graph(id='graph-vl', style={'height': '800px'}),
    ]),

])

@app.callback(
    Output('graph-vl', 'figure'),
    [Input('file-dropdown', 'value'), Input('tabs-vl', 'value'),]
)

def update_graph(selected_file, tab):
    if selected_file is None:
        return
    else:
        return plot_vl(selected_file, tab)

app.run_server(debug=True, port=8082)