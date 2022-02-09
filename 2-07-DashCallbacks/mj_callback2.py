import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = [{'label': str(year), 'value': year} for year in df['year'].unique()]
print(year_options)

app.layout = html.Div([
            dcc.Graph(id='graph'),
            dcc.Dropdown(id='year-picker',
                        options=year_options,
                        value=df['year'].min())
])

@app.callback(Output('graph', 'figure'),
                [Input('year-picker', 'value')])        # grab value from year-picker, output to figure from graph
def update_figure(selected_year):
    # data only for selected year
    filtered_df = df[df['year'] == selected_year]
    traces = []
    for continent in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent]
        traces.append(go.Scatter(x=df_by_continent['gdpPercap'],
                                y = df_by_continent['lifeExp'],
                                mode='markers',
                                opacity=0.7,
                                marker={'size': 15},
                                name=continent))
    return go.Figure(data=traces, layout=go.Layout(title='My Plot',
                                                    xaxis={'title': 'GDP Per Cap', 'type': 'log'},
                                                    yaxis={'title': 'Life Exp'}))

if __name__ == '__main__':
    app.run_server()
