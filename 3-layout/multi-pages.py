import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Input, Output

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#----------------------------------------------------------------#
# 1. Style                                                       #
#----------------------------------------------------------------#

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20%",
    "padding": "1rem 1rem",
    "background-color": "orange",
}

CONTENT_STYLE = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "80%",
    "padding": "1rem 1rem",
    "background-color":"green"
}


#----------------------------------------------------------------#
# 2. Interface                                                   #
#----------------------------------------------------------------#

sidebar = html.Div(
    [
        html.H2("Sidebar"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links"),
        dbc.Nav(
            children=[
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact")
            ],
            vertical=True,
            pills=True
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


#----------------------------------------------------------------#
# 3. Server                                                      #
#----------------------------------------------------------------#

@callback(
    Output("page-content", "children"),
    Input("url", "pathname")
    )
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        children=[
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run(debug=True)