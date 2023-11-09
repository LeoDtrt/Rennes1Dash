from dash import Dash, html, dcc, callback, Input, Output, State, dash_table
import base64
import datetime
import io
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Upload data csv example:"),
    dcc.Upload(id='upload', children=html.Button('upload')),    
    html.Div(id='out')
])

@callback(
    Output('out', 'children'),
    Input('upload', 'contents'),
    State('upload', 'filename'),
    State('upload', 'last_modified')
)
def update(c,n,d):
    if c is not None:
        content_type, content_string = c.split(',')              # Recuperation du contenu sans son type
        decoded = base64.b64decode(content_string)               # Decodage du contenu
        file = io.StringIO(decoded.decode('utf-8'))              # Recuperation du chemin et encodage UTF-8
        df = pd.read_csv(filepath_or_buffer=file, sep=';')       # Lecture du fichier csv avec séparateur ';'
        return html.Div([                                        # Preparation de la mise en page de la table
                    html.H5(n),
                    html.H6(datetime.datetime.fromtimestamp(d)),
                    dash_table.DataTable(
                        df.to_dict('records'),
                     [{'name': i, 'id': i} for i in df.columns]
                )])

if __name__ == '__main__':
    app.run(debug=True)

