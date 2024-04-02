from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from db_to_dash.db_to_dash_eis import test_list_eis, plot_eis

app = Dash(__name__)

app.title = 'AST-EIS'

app.layout = dbc.Container([

        html.Label("Select a file:"),
        dcc.Dropdown(
            id='file-dropdown',
            options=[{'label': test, 'value': test} for test in test_list_eis],
            value=test_list_eis[0],
            multi=False
        ),

    dbc.Row(dcc.Tabs(id='tabs-eis', value='2a', children=[
        dcc.Tab(label='2 A/cm2', value='2a'),
        dcc.Tab(label='1 A/cm2', value='1a'),
        dcc.Tab(label='0.1 A/cm2', value='01a'),
    ])),

    dbc.Row([
        dcc.Graph(id='graph-eis', style={'height': '800px'}),
    ]),

])

@app.callback(
    Output('graph-eis', 'figure'),
    [Input('file-dropdown', 'value'), Input('tabs-eis', 'value'),]
)

def update_graph(selected_file, tab):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return plot_eis(selected_file, tab)

app.run_server(debug=True,
               port=8086
               )

