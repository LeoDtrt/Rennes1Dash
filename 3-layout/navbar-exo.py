from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Iris Scatter", href="#scatter", external_link=True)),
        dbc.NavItem(dbc.NavLink("Iris Parallel", href="#parrallel", external_link=True)),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("ENT Rennes 1", href="https://ent.univ-rennes1.fr"),
                dbc.DropdownMenuItem("Github", href="https://github.com/"),
            ],
            nav=True,
            in_navbar=True,
            label="Liens Utiles",
        ),
    ],
    brand="Iris",
    brand_href="#scatter",
    brand_external_link=True,
    color="primary",
    dark=True,
)


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


content = html.Div([
    html.H1('Iris Scatter Plot', id='scatter'),
    html.Div(iris_scatter_content),
    html.H1('Iris Parrallel Coordinates', id='parrallel'),
    html.Div(iris_parrallel_content)
])

app.layout = html.Div([navbar, content])

if __name__ == '__main__':
    app.run(debug=True)

