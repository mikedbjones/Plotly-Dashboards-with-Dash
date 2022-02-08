import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)
x_values = np.linspace(0, 1, 100) # 100 evenly spaced points
y_values = np.random.randn(100) # 100 random normally distributed values

trace0 = go.Scatter(x=x_values, y=y_values+5,
                    mode='markers', name='markers') # use Scatter for line chart
                                                    # 'markers' will give just a scatter plot

trace1 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='mylines')

trace2 = go.Scatter(x=x_values, y=y_values-5,
                    mode='lines+markers', name='lines and markers')

data = [trace0, trace1, trace2] # instead of putting go.Scatter in here directly

layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='plot.html')
