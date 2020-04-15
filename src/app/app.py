import dash
import dash_core_components as dcc
import dash_html_components as html

from setup.db.raw.config import server, db

import pandas as pd
from setup.db.raw.models.replay.player import PLAYER

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
                    __name__, 
                    server = server, 
                    url_base_pathname = '/dashboard/', 
                    external_stylesheets=external_stylesheets
               )

pse = db.session.query(PLAYER).first().player_stats_events
df = pd.DataFrame([vars(i) for i in pse])[['second', 'food_made']]

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['second'], 'y': df['food_made'], 'type': 'bar', 'name': 'PSE'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
