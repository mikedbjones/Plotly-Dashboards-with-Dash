#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
                    dcc.RangeSlider(min=-5, max=5, step=1,
                                    value=[0, 0],
                                    marks={i: str(i) for i in range(-5, 6)},
                                    id='range-slider'),
                    html.H1(id='output')
])

# Create a Dash callback:

@app.callback(Output('output', 'children'),
                [Input('range-slider', 'value')])
def create_output(pair):
    return pair[0] * pair[1]

# Add the server clause:

if __name__ == '__main__':
    app.run_server()
