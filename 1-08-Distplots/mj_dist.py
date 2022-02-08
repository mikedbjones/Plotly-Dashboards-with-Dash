import plotly.offline as pyo
import plotly.figure_factory as ff # new import
import numpy as np

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1, x2, x3, x4]
group_labels = 'x1 x2 x3 x4'.split()

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2, .1, .3, .4])
pyo.plot(fig)
