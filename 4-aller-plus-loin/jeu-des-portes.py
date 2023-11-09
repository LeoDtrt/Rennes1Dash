from dash import Dash, dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
from random import sample

app = Dash(__name__)

gain = ['une voiture','une pomme','une seconde chance']

alea = sample(gain, 3)

opt = [{'label':f'Porte {i+1}','value':alea[i]} for i in range(len(alea))]

n_reset = []

app.layout = html.Div([
    html.H1("Jeu des Portes :"),
    
    dcc.RadioItems(id='radio', options=opt, value=None),
    dbc.Button(id='button', children="Rejouer", n_clicks=None),
    html.P(id='out')
])

@callback(
    Output('out','children'),
    Input('radio','value')
)
def update(value):
    if value is None:
        txt = "Sélectionnez une porte pour découvrir votre lot !"
    else:
        txt = f"Derrière cette porte se trouve {value}"
    return txt

@callback(
    Output('radio','options'),
    Output('radio', 'value'),
    Input('radio', 'options'),
    Input('button','n_clicks'),
    Input('radio', 'value'),
)
def update(opt, n, radio_value):
    if n is not None:
        if n > len(n_reset):
            n_reset.append(1)
            sample_opt = sample(opt, 3)
            opt = [{'label':f'Porte {i+1}','value':sample_opt[i]['value']} for i in range(len(sample_opt))]
            return opt, None
        else:
           return opt, radio_value            
    else:
        return opt, radio_value

if __name__ == '__main__':
    app.run(debug=True)