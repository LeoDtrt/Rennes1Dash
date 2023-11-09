from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

df = px.data.gapminder()
min_pop, max_pop = min(df['pop']), max(df['pop'])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Gapminder dataset :"),   
    dcc.Graph(id='graph-gdp', figure={}),
    dcc.RangeSlider(id='range-slider', min =min_pop , max=max_pop , value=[min_pop, max_pop], pushable=True)
])

@callback(
    Output(component_id='graph-gdp', component_property='figure'),
    Input(component_id='range-slider', component_property="value"),
)
def update_graph(value):
    df_update = df[(df['pop'] >= value[0]) & (df['pop'] <= value[1])]    
    fig = px.scatter(df_update.query("year==2007"), 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title='Life expectancy by GDP per capita and population in 2007')
    return fig

if __name__ == '__main__':
    app.run(debug=True)

