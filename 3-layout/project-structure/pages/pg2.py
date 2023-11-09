from dash import html, register_page


register_page(__name__,
    name='Page 2'
)


layout = html.Div([
        
    # Titre
    html.H1("Text Creation")
    
])



