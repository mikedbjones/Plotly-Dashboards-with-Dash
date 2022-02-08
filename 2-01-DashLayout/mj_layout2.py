import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[                # H1, Div, etc are HTML components
            html.H1('Hello Dash!', style={'textAlign': 'center',
                                            'color': colors['text']}),
            dcc.Graph(id='example',             # from dash_core_components
                    figure={'data': [
                        {'x':[1,2,3], 'y':[4,1,2], 'type': 'bar', 'name': 'SF'},
                        {'x':[1,2,3], 'y':[2,4,5], 'type': 'bar', 'name': 'NYC'}
                    ],
                            'layout': {
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {'color': colors['text']},
                            'title': 'Bar plots'
                            }})           # data, layout from plotly
], style={'backgroundColor':colors['background']}
)

if __name__ == '__main__': # ie, if running script directly
    app.run_server()
