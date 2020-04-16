import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.app.app import app
from src.app.utils.replay import construct_replay_table

layout = html.Div( 
                    [
                        html.H2(
                            'Replays', 
                            style = {
                                        'width': '100%', 
                                        'display': 'flex', 
                                        'align-items': 'center', 
                                        'justify-content': 'center'
                                     }
                                ),
                        html.Div( children = [
                                                 construct_replay_table()
                                              ],
                                  style = {
                                            'width': '100%', 
                                            'display': 'flex', 
                                            'align-items': 'center', 
                                            'justify-content': 'center'
                                          }
                                 )
                    ]
                 )


