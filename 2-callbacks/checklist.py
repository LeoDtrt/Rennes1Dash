from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

opt = ['Choix 1', 'Choix 2', 'Choix 3']

app.layout = html.Div([
    html.H1('Checklist example :'),
    dcc.Checklist(id='checklist', options=opt, value=opt),
    html.H4("Valeurs sélectionnées dans la checklist :"),
    html.P(id='state-out', children='')
    
])

@callback(
    Output('state-out', 'children'),
    Input('checklist', 'value')
)
def update_state(values):
    return [html.Li(val) for val in values]

if __name__ == '__main__':
    app.run(debug=True)

    