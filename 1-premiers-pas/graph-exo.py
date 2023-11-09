from dash import Dash, html, dcc
import plotly_express as px

app = Dash(__name__)

df = px.data.iris()

lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

fig = px.parallel_coordinates(df, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)

app.layout = html.Div([
    
    html.H1('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='parallel-coord', figure=fig)

])

if __name__ == '__main__':
    app.run(debug=True)