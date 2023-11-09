from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__)

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
opt = df.continent.unique()

# Definition de l'etat initial de la checklist
etat_initial = ['Asia']

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#

app.layout = html.Div([
    
    # Titre de l'application
    html.H1("Gapminder dataset : Checklist & Slider"),
    
    # Dropdown permettant de selectionner les continents
    dcc.Checklist(id="checklist", options=opt, value=etat_initial, inline=True),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
               marks=slider_marks, step = None)
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#

@callback(
    Output(component_id='graph-gdp', component_property='figure'),
    Input(component_id='slider', component_property="value"),
    Input(component_id='checklist', component_property="value")
)
def update_graph(year_value, continent_value):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[0, 100])
    return fig

#-----------------------------------------------------------------------#
# Run                                                                   #
#-----------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)

