import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State          # added State here

app = dash.Dash()

app.layout = html.Div([
                        dcc.Input(id='number-in',
                                    value=1,
                                    style={'fontSize': 24}),
                        html.Button(id='submit-button',
                                    n_clicks=0,             # tracks number of clicks
                                    children='Submit Here',
                                    style={'fontSize': 24}),
                        html.H1(id='number-out')
])

@app.callback(Output('number-out', 'children'),
                [Input('submit-button', 'n_clicks')],
                [State('number-in', 'value')])                                  # State also goes in a list
def output(n_clicks, number):
    return f"{number} was typed in; {n_clicks} clicks were made"

if __name__ == '__main__':
    app.run_server()
