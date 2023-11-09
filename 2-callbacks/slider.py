from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Numeric slider from -10 to 10 by 2 and begin with 8 :"),
    dcc.Slider(id="slider-numeric", min = -10, max=10, value=8, step = 2),
    
    html.H1("String slider from State 1 to 10 begin with State 2 :"),
    dcc.Slider(id ="slider-string", min=0, max=9, marks={i: f'State{i}' for i in range(10)}, value=2),
    
    html.H1("Range slider from 0 to 10K by 1K begin between 1K and 5K :"),
    dcc.RangeSlider(id ="slider-range", min=0, max=10000, step=1000, value=[1000,5000])

])

if __name__ == "__main__":
    app.run(debug=True)

