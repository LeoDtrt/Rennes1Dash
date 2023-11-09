from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([

    html.Header("Header", style={'borderStyle':'dotted'}),
    
    html.H1("Titre Niveau 1", style={'color':'blue'}),
    
    html.H2("Titre Niveau 2", style={'backgroundColor':'orange'}),
            
    html.H3("Titre Niveau 3", style={'textDecoration' : 'green wavy underline'}),
    
    html.Br(),

    html.P("Paragraphe 1", style={'textAlign': 'center'}),    
    
    html.Hr(),
    
    html.P("Paragraphe 2", style={'textAlign': 'end'}),  
    
    html.Hr(),
        
    html.P("Paragraphe 3", style={'marginLeft':'100px'})

    
])

if __name__ == '__main__':
    app.run(debug=True)
    
    
    