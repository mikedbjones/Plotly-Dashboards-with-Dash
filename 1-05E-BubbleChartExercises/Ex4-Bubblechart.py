#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go



# create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['displacement'],
                    y=df['acceleration'],
                    mode='markers',
                    text=df['name'],
                    marker=dict(size=df['mpg']))]







# create a layout with a title and axis labels
layout = go.Layout(title='Displacement vs Acceleration', hovermode='closest')






# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble.html')
