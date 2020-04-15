import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.app.app import app
from src.app.utils.replay import construct_replay_table

from src.db.raw.config import db
from src.db.raw.create import *

query_info = db.session.query(INFO).all()

layout = html.Div( 
                    [
                        html.H2('Replays'),
                        html.Div(
                                    construct_replay_table(query_info)
                                )
                    ]
                        
                 )


