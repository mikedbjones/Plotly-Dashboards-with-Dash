import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../data/mpg.csv')

data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'], # determines hover values
                    mode='markers',
                    marker=dict(size=df['weight']/100, # used /100 for better scaling
                                color=df['cylinders'],
                                showscale=True),
                    )]
                    # here we're getting 4 dimensions of info on only a 2d plot using bubbles and colours

layout = go.Layout(title='Bubble Chart', hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bubbleplot.html')
