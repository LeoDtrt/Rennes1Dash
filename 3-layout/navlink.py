from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Doc Dash", active=True, href="https://dash.plotly.com/")),
        dbc.NavItem(dbc.NavLink("Target 1", href="#target1", external_link=True)),
        dbc.NavItem(dbc.NavLink("Target 2", href="#target2", external_link=True)),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Github", href="https://github.com/"),
             dbc.DropdownMenuItem("Gitlab", href="https://about.gitlab.com/")],
            label="Dropdown",
            nav=True,
        ),
    ]
)

content = html.Div([
    html.Div([html.H1("Titre") for x in range(20)]),
    html.H1('Target 1', id='target1'),
    html.Div([html.H1("Titre") for x in range(20)]),
    html.H1('Target 2', id='target2'),
])

app.layout = html.Div([nav, content])

if __name__ == '__main__':
    app.run(debug=True)

