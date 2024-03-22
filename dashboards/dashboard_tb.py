from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from db_to_dash.db_to_dash_tb import test_list_tb, plot_tb

app = Dash(__name__)

app.title = 'AST-TB'

# data_folder = 'data'
# files = [f for f in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, f))]

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
        return plot_tb(selected_file)


app.run_server(debug=True, port=8080)