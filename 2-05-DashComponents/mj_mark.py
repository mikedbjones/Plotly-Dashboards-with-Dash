import dash
import dash_html_components as html
import dash_core_components as dcc

markdown_text = '''
Here is some markdown text with **bold**, *italic* and other things like [links to stuff](https://commonmark.org).
I think this is cool because
1. It is
1. It definitely is

Nice one!
- You can go now
'''

app = dash.Dash()

app.layout = html.Div([dcc.Markdown(children=markdown_text)])

if __name__ == '__main__':
    app.run_server()
