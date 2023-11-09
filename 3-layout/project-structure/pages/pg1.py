from dash import dcc, html, register_page


register_page(__name__,
    path='/',
    name='Page 1'
)

layout = html.Div([
    
    # Titre
    dcc.Markdown('# Iris Dataset')
    
])


