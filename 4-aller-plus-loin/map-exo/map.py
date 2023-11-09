from dash import Dash, dcc, html, Input, Output
import plotly_express as px
import pandas as pd
import json
import dash_daq as daq
import dash_bootstrap_components as dbc


file1 = "./dep_fr.geojson"
file2 = "./FD_MAR_2018.csv"
titre = "Nombre de mariages en France par département en 2018"



# Importation fichier geojson
with open(file1) as f:
    geo = json.load(f)
    

# Importation du dataframe 
df = pd.read_csv(file2, sep=";", low_memory=False)
variable = 'DEPMAR'
df = df.groupby([variable])[variable].count()
df = pd.DataFrame(df)
df.rename(columns={variable:'NBMAR'}, inplace=True)
df.reset_index(inplace=True)

# Initialisation de la css
external_css = [dbc.themes.CERULEAN]

# Initialisation de l'app
app = Dash(__name__,
           external_stylesheets=external_css)

# Definition du style du color-picker
picker_style = {"display":"inline-block", "margin":10}

app.layout = dbc.Container([
    
    dbc.Row([
        html.H4('Cartographie GEOJSON'),
        html.P(titre)
    ]),
    
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph')
        ], width=7),
        
        dbc.Col([
            html.H4('Interactive color picker with Dash'),
            daq.ColorPicker(id='color-min',
                            label='Color Min',
                            size = 150,
                            style = picker_style,
                            value=dict(kex='#F1F1ED')),
            
            daq.ColorPicker(id='color-max',
                            label='Color Max',
                            size = 150,
                            style = picker_style,
                            value=dict(kex='#1E347C'))
            
        ], width=5)
    ])
], fluid=True)


@app.callback(
    Output('graph', 'figure'),
    Input('color-min','value'),
    Input('color-max','value')
)
def display_choropleth(color_min, color_max):
    
    key_min = [x for x in color_min.keys()][0]
    key_max = [x for x in color_max.keys()][0]
    
    fig = px.choropleth(
        df,
        geojson=geo,
        color = 'NBMAR',
        locations='DEPMAR',
        featureidkey='properties.code',
        projection='mercator',
        range_color=[df['NBMAR'].min(), df['NBMAR'].max()],
        width=800,
        height=600,
        color_continuous_scale=[[0, color_min[key_min]],
                                [1, color_max[key_max]]]
    )
    fig.update_geos(fitbounds='locations', visible=False)
    fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    
