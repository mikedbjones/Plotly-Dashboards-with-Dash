import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

            html.Label('Dropdown'),
            dcc.Dropdown(options=[{'label': 'New York City',    # options is a list of dicts
                                    'value': 'NYC'},
                                    {'label': 'San Francisco',
                                                            'value': 'SF'}],
                                value='SF'),                     # value is default value, in this case SF
            html.Label('Slider'),
            dcc.Slider(min=-10, max=10, step=0.5, value=0,
                        marks={i: i for i in range(-10, 11)}),      # value is default value
            html.P(html.Label('Some Radio Items')),     # paragraph to fix spacing issue. Better way to fix would be to use a div and some style calls
            dcc.RadioItems(options=[{'label': 'New York City',    # options is a list of dicts
                                    'value': 'NYC'},
                                    {'label': 'San Francisco',
                                                            'value': 'SF'}],
                                    value='SF')
])

if __name__ == '__main__':
    app.run_server()
