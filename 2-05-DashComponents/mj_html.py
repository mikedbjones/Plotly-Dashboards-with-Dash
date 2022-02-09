import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['This is the outermost div',             # if you have multiple components inside div, you need a list
                        html.Div('This is an inner div',        # otherwise you don't
                        style={'color': 'red', 'border': '2px red solid'}),
                        html.Div(['Another inner div'],
                        style={'color': 'blue', 'border': '3px blue solid'}
                        )],
                        style={'color': 'green',
                                'border': '2px green solid'})

if __name__ == '__main__':
    app.run_server()
