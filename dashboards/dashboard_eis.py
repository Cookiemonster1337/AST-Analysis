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

    dbc.Row([
        dcc.Graph(id='graph-eis', style={'height': '800px'}),
    ]),

])

@app.callback(
    Output('graph-eis', 'figure'),
    [Input('file-dropdown', 'value')]
)

def update_graph(selected_file):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return plot_eis(selected_file)

app.run_server(debug=True,
               port=8086
               )

