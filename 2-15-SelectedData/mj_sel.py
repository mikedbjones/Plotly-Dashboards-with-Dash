import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

app = dash.Dash()

np.random.seed(10)
x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

# DFs
df1 = pd.DataFrame({'x': x1, 'y': y})
df2 = pd.DataFrame({'x': x1, 'y': y})
df3 = pd.DataFrame({'x': x2, 'y': y})

df = pd.concat([df1, df2, df3])

app.layout = html.Div([
    html.Div([dcc.Graph(id='plot',
                figure={'data': [go.Scatter(
                                x = df['x'],
                                y = df['y'],
                                mode='markers'
                )],
                        'layout': go.Layout(title='Scatterplot',
                                            hovermode='closest')})],
            style={'width': '30%', 'display': 'inline-block'}),
    html.Div([
            html.H1(id='density', style={'paddingTop': 25})
    ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),

])


@app.callback(Output('density', 'children'),
                [Input('plot', 'selectedData')])
def find_density(selectedData):                             # my code simpler, only for box selects
    n_points = len(selectedData['points'])
    x_len = selectedData['range']['x'][1] - selectedData['range']['x'][0]
    y_len = selectedData['range']['y'][1] - selectedData['range']['y'][0]
    d = n_points/(x_len*y_len)
    return f"Density: {d:.2f}"

if __name__ == '__main__':
    app.run_server()
