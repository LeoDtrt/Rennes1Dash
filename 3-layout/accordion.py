from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    dbc.Accordion([
        dbc.AccordionItem(
            title="Item 1", 
            children=[
                html.P("This is the content of the first section"),
                dbc.Button("Click here")
            ]
        ),
        
        dbc.AccordionItem(
            title="Item 2",
            children=[
                html.P("This is the content of the second section"),
                dbc.Button("Don't click me!", color="danger"),
            ]
        ),
        
        dbc.AccordionItem(
            title="Item 3",
            children="This is the content of the third section"
        )
    ])
)

if __name__ == '__main__':
    app.run(debug=True)
    
