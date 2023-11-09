from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

# Recuperation du dataset Gapminder
df = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = df.year.min(), df.year.max()

# Creation des markers pour le slider sur les annees
slider_marks = {str(year): str(year) for year in df.year.unique()}

# Recuperation de la liste des continents 
opt_continent = df.continent.unique()

# Creation des options du radio items pour l'activation du logarithme sur l'axe des x
opt_log = [{'label': 'Activée', 'value': True}, {'label': 'Désactivée', 'value': False}]

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#

tab1_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent, inline=True)]
    )
)

tab2_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.RadioItems(id='radio', options=opt_log, value=True)]
    )
)

tab3_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
                             marks=slider_marks, step = None)]
    )
)



app.layout = html.Div([
    
    # Titre de l'application
    html.H1("Gapminder dataset : Checklist & Slider"),
    
    dbc.Tabs(
        id="tabs",
        children=[
            dbc.Tab(label="Sélection des continents", tab_id="tab-1",
                    children=tab1_content),
            dbc.Tab(label="Transformation logarithmique du PIB par tête (gdpPercap)", tab_id="tab-2",
                    children=tab2_content),
            dbc.Tab(label="Sélection de l'année", tab_id="tab-3",
                    children=tab3_content)
        ],
        active_tab="tab-1"),
    html.Div(id="content"),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={}),
        
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


@callback(
    Output('graph-gdp', 'figure'),
    Input('slider', "value"),
    Input('checklist', "value"),
    Input('radio', 'value')
)
def update_graph(year_value, continent_value, log_boolean):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=log_boolean,
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    if log_boolean:
        fig.update_xaxes(type="log", range=[2,5])
    else :
        fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[20, 100])

    return fig

#-----------------------------------------------------------------------#
# Run                                                                   #
#-----------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)

