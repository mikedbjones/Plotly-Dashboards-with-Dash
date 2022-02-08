#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd



# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')
classes = df['class'].unique()


# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
hist_data = []
group_labels = []
for c in classes:
    hist_data.append(df[df['class']==c]['petal_length'])
    group_labels.append(c)

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig)



# Define a data variable



# Create a fig from data and layout, and plot the fig
