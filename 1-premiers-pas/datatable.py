from dash import Dash, html, dash_table
import plotly.express as px
import pandas as pd

df = pd.DataFrame(px.data.iris())

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Iris Dataset"),
    
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={"borderStyle": "groove"},
        page_size=10
)
    
])

if __name__ == '__main__':
    app.run(debug=True)
    
    
    