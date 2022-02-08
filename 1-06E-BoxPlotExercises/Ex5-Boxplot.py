#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd




# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')


# take two random samples of different sizes:
sample1 = df['rings'].sample(50, replace=False)
sample2 = df['rings'].sample(100, replace=False)


# create a data variable with two Box plots:
data = [go.Box(y=sample1, name='a'),
        go.Box(y=sample2, name='b')]










# add a layout
layout = go.Layout(title='2 random samples of rings from Abalone dataset')



# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
