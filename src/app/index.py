import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.app.app import app
from src.app.apps import app1, app2, replays

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

## match the first elements on here and then 
## populate a page on the remaining information
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/replay':
        print(pathname)
        return replays.layout
    else:
        return '404'

app.run_server(debug=True)
