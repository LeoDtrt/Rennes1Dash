from dash import dcc, html, register_page


register_page(__name__,
    name='Page 3'
)

layout = html.Div([
    
    html.Div([
        dcc.Markdown("Description Box")
    ], className="kri-box-description"),
    
    html.Div([
         dcc.Markdown("Control Box")
    ], className="kri-box-control"),
    
    html.Div([
        dcc.Markdown("Selection Box")
    ], className="kri-box-selection"),
    
    html.Div([
        dcc.Markdown("Table Box")
    ], className="kri-box-table"),
    
    html.Div([
        dcc.Markdown("Graph Box")
    ], className="kri-box-graph")
    
], className = 'wrapper')

