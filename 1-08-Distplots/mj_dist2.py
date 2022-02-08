import plotly.offline as pyo
import plotly.figure_factory as ff # new import
import numpy as np

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]
# frequency of 3 letter words in works by snodgrass vs works by twain

hist_data = [snodgrass, twain]
group_labels = ['Snodgrass', 'Twain']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.005, .005])
pyo.plot(fig)
