from dash import Dash, html, callback, Input, Output, dcc

app = Dash(__name__)

opt = ['Choix 1', 'Choix 2', 'Choix 3']

app.layout = html.Div([
    html.H1("Simple dropdown choice :"),
    dcc.Dropdown(id="dropdown", options=opt, value=opt[0]),
    
    html.H1("Multi dropdown choice :"),
    dcc.Dropdown(id="dropdown-multi", options=opt, value=opt[0], multi=True)
])

if __name__ == "__main__":
    app.run(debug=True)



