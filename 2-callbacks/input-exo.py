from dash import Dash, dcc, html, callback, Input, Output

app = Dash(__name__)

txt = []

app.layout = html.Div([
    html.H1("Ecriture d'un texte :"),
    dcc.Input(id='input-text',type='text', debounce=True),
    html.P(id='out',children='')
])

@callback(
    Output('out', 'children'),
    Input('input-text', 'value')
)
def create_txt(value):
    if value is not None:
        txt.append(html.Li(value))
        return txt

if __name__ == '__main__':
    app.run(debug=True)

