from dash import Dash, dcc, html, callback, Input, Output

#------------------------------------------------------------#
# 1. INITIALISATION                                          #
#------------------------------------------------------------#

app = Dash(__name__)

txt = []
n = []

#------------------------------------------------------------#
# 2. INTERFACE                                               #
#------------------------------------------------------------#

app.layout = html.Div([
    
    # Title
    html.H1("Application permettant la création et l'exportation d'un fichier txt :"),
    
    # Download txt
    html.Button(id='btn-download-txt', children='Download Text'),
    dcc.Download(id='download-text'),    
    dcc.Input(id='name-download-file', type='text', debounce=True, value='Filename'),
    
    html.Br(),
    
    # Create txt
    html.H4("Saisie du texte:"),
    dcc.Input(id='input-text', type='text', debounce=True),
    html.P(id='text',children='')
])

#------------------------------------------------------------#
# 3. CREATE TEXT                                             #
#------------------------------------------------------------#

@callback(
    Output('text', 'children'),
    Input('input-text', 'value')
)
def create_txt(value):
    if value is not None:
        txt.append(html.Li(value))
        return txt

#------------------------------------------------------------#
# 4. DOWNLOAD TEXT                                           #
#------------------------------------------------------------#

@callback(
    Output('download-text', 'data'),
    Input('btn-download-txt', 'n_clicks'),
    Input('text','children'),
    Input('name-download-file', 'value'),
)
def download_txt(n_clicks, text, filename):
    if n_clicks is not None:
        if n_clicks > len(n):
            if text is not None:
                txt = [x['props']['children'] for x in text]
                txt = '\n'.join(txt)
                n.append(n_clicks)
                return dict(content=txt, filename=filename+".txt")

if __name__ == '__main__':
    app.run(debug=True)

