from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

input_types = ("text", "number", "password", "email",
               "search", "tel", "url", "range", "hidden")

app.layout = html.Div(
    [
        dcc.Input(
            id="input_{}".format(x),
            type=x,
            placeholder="input type {}".format(x),
        )
        for x in input_types
    ]
    + [html.Div(id="out-all-types")]
)

@callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(x), "value") for x in input_types],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


if __name__ == "__main__":
    app.run(debug=True)

