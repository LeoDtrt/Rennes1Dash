from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    
    html.Header([
        html.H1('Segmentation de ma page Web :')
        ]),
    
    dbc.Row([
        dbc.Col(html.Div("Zone A"), align="start" , style={'backgroundColor':'green'}),
        dbc.Col(html.Div("Zone B"), align="center", style={'backgroundColor':'red'}),
        dbc.Col(html.Div("Zone C"), align="end"   , style={'backgroundColor':'pink'}),
        ], style={'height': '120px', 'borderStyle': 'dotted'}),
    

    
    dbc.Row([
                dbc.Col(html.Div("Zone D"), align="start" , style={'backgroundColor':'blue', 'height': '100%'}, width=2),
                dbc.Col(html.Center("Zone E"), align="center", style={'backgroundColor':'yellow', 'height': '50%'}, width=9),
                dbc.Col(html.Div("Zone F"), align="end"   , style={'backgroundColor':'orange'}, width=1),
            ], style={'height': '200px', 'borderStyle': 'double'})
    
])

if __name__ == '__main__':
    app.run(debug=True)
    
