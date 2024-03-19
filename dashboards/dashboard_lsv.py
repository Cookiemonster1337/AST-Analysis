from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from db_to_dash.db_to_dash_lsv import test_list_cv, plot_lsv

app = Dash(__name__)

app.title = 'AST-LSV'

app.layout = dbc.Container([

    html.Label("Select file:"),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': test, 'value': test} for test in test_list_cv],
        value=test_list_cv[0],
        multi=False
    ),

    # TB-PLOT
    dbc.Row([
        dcc.Graph(id='graph-lsv', style={'height': '800px'}),
    ]),

])

@app.callback(
    Output('graph-lsv', 'figure'),
    [Input('file-dropdown', 'value')]
)


def update_graph(selected_file):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return plot_lsv(selected_file)


app.run_server(debug=True, port=8080)