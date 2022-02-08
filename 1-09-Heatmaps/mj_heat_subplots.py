import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools # for subplots
import pandas as pd

df1 = pd.read_csv('../data/2010SitkaAK.csv')
df2 = pd.read_csv('../data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('../data/2010YumaAZ.csv')

dfs = [df1, df2, df3]
data = []
for df in dfs:
    data.append(go.Heatmap(x=df['DAY'], y=df['LST_TIME'],
                        z=df['T_HR_AVG'].values.tolist(),
                        colorscale='Jet',
                        zmin=5, zmax=40))

fig = tools.make_subplots(rows=1, cols=3, subplot_titles=['Sitka AK', 'SB CA', 'Yuma AZ'],
                            shared_yaxes=True) # so we don't get more than 1 y axis

fig.append_trace(data[0], 1, 1) # trace, row, column
fig.append_trace(data[1], 1, 2)
fig.append_trace(data[2], 1, 3)

fig['layout'].update(title='Temps for 3 cities')
pyo.plot(fig)
