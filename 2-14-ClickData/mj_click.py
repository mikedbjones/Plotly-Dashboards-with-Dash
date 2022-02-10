import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

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
                    html.Div(html.Img(id='hover-data', src='children', height=300),
                            style={'paddingTop': 35})
])

@app.callback(Output('hover-data', 'src'),
                [Input('wheels-plot', 'clickData')])                                            # clickData is a property of dcc.Graph objects
def callback_image(clickData):
    wheel = clickData['points'][0]['y']
    color = clickData['points'][0]['x']
    path = '../data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()
