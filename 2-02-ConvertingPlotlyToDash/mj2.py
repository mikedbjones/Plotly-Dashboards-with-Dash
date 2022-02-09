import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating data

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x, y=random_y, mode='markers',
                    marker={'size': 12,
                            'color': 'rgb(51,204,153)',
                            'symbol': 'pentagon',
                            'line': {'width': 2}})]

data2 = [go.Scatter(x=random_x, y=random_y, mode='markers',
                    marker={'size': 22,
                            'color': 'rgb(22,96,124)',
                            'symbol': 'circle',
                            'line': {'width': 2}})]

layout = go.Layout(title='Scatter plot', xaxis={'title': 'My axis title'})



app.layout = html.Div([dcc.Graph(id='scatterplot',              # Graph has id and figure
                                figure={'data': data,            # Graph sits inside a list in html.Div()
                                        'layout': layout}),
                        dcc.Graph(id='scatterplot2',
                                                        figure={'data': data2,
                                                                'layout': layout})])

if __name__ == '__main__':
    app.run_server()
