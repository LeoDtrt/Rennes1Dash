from dash import Dash, html, callback, Input, Output, dcc

# Initialisation de l'application
app = Dash(__name__)

# Initialisation des variables
choix_possibles = ['Choix 1','Choix 2', 'Choix 3']
etat_initial = choix_possibles[0]

# Creation de l'interface de l'application
app.layout = html.Div([
    
    # Titre de l'application
    html.H1("My firt callback with dash"),
    
    # Objet permettant de selectionner un input
    dcc.Dropdown(id='nom-objet-input',
                 options=choix_possibles,
                 value=etat_initial),

    # Objet qui se met a jour suivant l'etat de l'input
    html.Div(id='nom-objet-output')
])

# Serveur de l'application permettant la mise a jour dynamique
@callback(
    Output(component_id='nom-objet-output', component_property='children'),
    Input(component_id='nom-objet-input' , component_property='value')
)
def update_objet_en_sortie(value):
    return f"Nouvel état de l'objet en sortie: {value}"

# Code permettant de run l'application
if __name__ == "__main__":
    app.run(debug=True)

