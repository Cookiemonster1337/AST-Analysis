from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from db_to_dash.db_to_dash_asr import test_list_asr, plot_asr


app = Dash()

app.title = 'ASR'

app.layout = dbc.Container([

    html.Label("Select file:"),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': test, 'value': test} for test in test_list_asr],
        value=test_list_asr[0],
        multi=False
    ),

    # ASR-PLOT
    dbc.Row([
        dcc.Graph(id='graph-asr', style={'height': '800px'}),
    ]),

])

@app.callback(
    Output('graph-asr', 'figure'),
    [Input('file-dropdown', 'value')]
)


def update_graph(selected_file):
    if selected_file is None:
        return
    else:
        print(selected_file)
        return plot_asr(selected_file)


app.run_server(debug=True, port=8084)