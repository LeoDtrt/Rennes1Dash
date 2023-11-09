from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([

    html.Header("Header"),
    
    html.H1("Titre Niveau 1"),
    
    html.H2("Titre Niveau 2"),
            
    html.H3("Titre Niveau 3"),
    
    html.Br(),

    html.P("Paragraphe 1"),    
    
    html.Hr(),
    
    html.P("Paragraphe 2"),  
    
    html.Hr(),
        
    html.P("Paragraphe 3")

    
])

if __name__ == '__main__':
    app.run(debug=True)
    
    
    