import plotly.offline as pyo
import plotly.graph_objs as go

# in box plots, outlying values lie outside the IQR by at least 1.5*IQR

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]
# frequency of 3 letter words in works by snodgrass vs works by twain

data = [go.Box(y=snodgrass, name='Snodgrass'),
        go.Box(y=twain, name='Twain')]

pyo.plot(data)
