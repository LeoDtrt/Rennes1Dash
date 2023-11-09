import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Input, Output
import plotly.express as px

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
    "background-color": "#003366",
}

CONTENT_STYLE = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "padding": "1rem 1rem",
    "width": "80%",
}


#----------------------------------------------------------------#
# 2. Pages                                                       #
#----------------------------------------------------------------#

df = px.data.iris()

fig1 = px.scatter(df, x="sepal_width", y="petal_length", color="species")

iris_scatter_content = html.Div(children=[
    html.H3(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='graph1', figure=fig1)
])

lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

fig2 = px.parallel_coordinates(df, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)

iris_parrallel_content = html.Div([
    
    html.H3('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='graph2', figure=fig2)

])


#----------------------------------------------------------------#
# 3. Interface                                                   #
#----------------------------------------------------------------#

sidebar = html.Div(
    [
        html.H2("IRIS DATASET", style={"color":"white"}),
        html.Hr(),
        dbc.Nav(
            children=[
                dbc.NavLink("Presentation", href="/", active="exact"),
                dbc.NavLink("Iris Scatter Plot", href="/page-1", active="exact"),
                dbc.NavLink("Iris Parrallel Plot", href="/page-2", active="exact")
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
        return html.P("This is a very short presentation.")
    elif pathname == "/page-1":
        return iris_scatter_content
    elif pathname == "/page-2":
        return iris_parrallel_content
    
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