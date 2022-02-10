import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
df['year'] = random.randint(-4, 5, len(df))*0.1 + df['model_year']      # adds jitter so years aren't just whole numbers. Controversial as it's faking the data!

app.layout = html.Div([
                        dcc.Graph(id='mpg-scatter',
                                    figure={'data': [go.Scatter(x=df['year']+1900,
                                                                y=df['mpg'],
                                                                text=df['name'],
                                                                hoverinfo='text'+'y'+'x',
                                                                mode='markers')],
                                            'layout': go.Layout(title='MPG Data',
                                                                xaxis={'title': 'Model Year'},
                                                                yaxis={'title': 'MPG'},
                                                                hovermode='closest')})
])

if __name__ == '__main__':
    app.run_server()
