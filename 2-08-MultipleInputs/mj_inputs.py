import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

app = dash.Dash()

features = df.columns

app.layout = html.Div([
                html.Div([
                    dcc.Dropdown(id='xaxis',
                                options=[{'label': i, 'value': i} for i in features],
                                value='displacement')
                ], style={'width': '48%', 'display': 'inline-block'}),  # inline-block allows dropdowns to be adjacent
                html.Div([
                    dcc.Dropdown(id='yaxis',
                                options=[{'label': i, 'value': i} for i in features],
                                value='mpg')
                ], style={'width': '48%', 'display': 'inline-block'}),
                dcc.Graph(id='feature-graphic')
], style={'padding': 10})

@app.callback(Output('feature-graphic', 'figure'),
                [Input('xaxis', 'value'), Input('yaxis', 'value')])
def update_plot(x, y):
    data = [go.Scatter(x=df[x], y=df[y], text=df['name'],
                        mode='markers', marker={'size': 15, 'opacity': 0.7,
                                                'line': {'width': 0.5, 'color': 'black'}})]
    layout = go.Layout(title='Car Scatter Plot',
                        xaxis={'title': x},
                        yaxis={'title': y},
                        hovermode='closest')
    return {'data': data,'layout': layout}

if __name__ == '__main__':
    app.run_server()
