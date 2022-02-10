import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('../data/wheels.csv')

app.layout = html.Div([
                    html.Div(dcc.Graph(id='wheels-plot',
                                        figure={'data': [go.Scatter(x=df['color'],
                                                                    y=df['wheels'],
                                                                    dy=1,                       # to give grid pattern
                                                                    mode='markers',
                                                                    marker={'size': 15})],
                                                'layout': go.Layout(title='Test',
                                                                    hovermode='closest')}),
                            style={'width': '30%', 'float': 'left'}),
                    html.Div(html.Pre(id='hover-data', style={'paddingTop': 35}),               # pre formatted html component
                            ),
])

@app.callback(Output('hover-data', 'children'),
                [Input('wheels-plot', 'hoverData')])                                            # hoverData is a property of dcc.Graph objects
def callback_image(hoverData):
    return json.dumps(hoverData, indent=2)

if __name__ == '__main__':
    app.run_server()
