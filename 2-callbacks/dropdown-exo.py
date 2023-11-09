from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

var = [{'label':s.replace('_',' ').capitalize(),'value':s}  for s in df.columns[0:3]]

app.layout = html.Div(children=[
    html.H1(children='Dash: A web application framework for your data.'),
    
    html.H4('Horizontal scale :'),
    dcc.Dropdown(id='x', options=var, value=var[0]['value']),
    
    html.H4('Vertical scale :'),
    dcc.Dropdown(id='y', options=var, value=var[1]['value']),
    
    dcc.Graph(figure={}, id='scatter')
])


@callback(
    Output(component_id='scatter', component_property='figure'),
    Input(component_id='x', component_property='value'),
    Input(component_id='y', component_property='value'),
)
def update_graph(x, y):
    fig = px.scatter(df, x=x, y=y, color="species",
                     labels={
                         x:x.replace('_',' ').capitalize(),
                         y:y.replace('_',' ').capitalize(),
                        },
                     title="Scatter Plot of the Iris Dataset")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
    
    
