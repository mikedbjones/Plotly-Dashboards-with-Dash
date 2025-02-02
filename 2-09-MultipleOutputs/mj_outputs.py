import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('../data/wheels.csv')

app = dash.Dash()

app.layout = html.Div([
            dcc.RadioItems(id='wheels', options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                            value=1),
            html.Div(id='wheels-output'),
            html.Hr(),              # horizontal line
            dcc.RadioItems(id='colors', options=[{'label': i, 'value': i} for i in df['color'].unique()],
                            value='blue'),
            html.Div(id='colors-output')
], style={'fontFamily': 'helvetica', 'fontSize': 18})

@app.callback(Output('wheels-output', 'children'),
                [Input('wheels', 'value')])
def callback_a(wheels):
    return f"You chose {wheels}"

@app.callback(Output('colors-output', 'children'),
                [Input('colors', 'value')])
def callback_b(colors):
    return f"You chose {colors}"

if __name__ == '__main__':
    app.run_server()
