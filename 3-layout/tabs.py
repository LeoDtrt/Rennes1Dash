import dash_bootstrap_components as dbc
from dash import Dash, html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

tab1_content = dbc.Card(
    dbc.CardBody([
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]),
    className="mt-3"
)

tab2_content = dbc.Card(
    dbc.CardBody([
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]),
    className="mt-3",
)

app.layout = html.Div([
    dbc.Tabs([
            dbc.Tab(label="Tab 1", tab_id="tab-1", children=tab1_content),
            dbc.Tab(label="Tab 2", tab_id="tab-2", children=tab2_content),
        ],
        id="tabs",
        active_tab="tab-1"
    ),
    html.Div(id="content")
])

if __name__ == '__main__':
    app.run(debug=True)

