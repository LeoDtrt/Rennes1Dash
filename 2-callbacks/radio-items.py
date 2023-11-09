from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

opt = [{'label':f'Choix {i}','value':i} for i in range(1,4)]

app.layout = html.Div([
    
    html.H1("Radio Items examples:"),
    
    dcc.RadioItems(id='radio', options=opt, value=None),
    
    html.P(id='out')
])

@callback(
    Output('out','children'),
    Input('radio','value')
)
def update(value):
    if value is None:
        txt = "Aucun choix n'a encore été sélectionné."
    else:
        txt = f"Le choix numéro {value} a été sélectionné !"
    return(txt)

if __name__ == '__main__':
    app.run(debug=True)

