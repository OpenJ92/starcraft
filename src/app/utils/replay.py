import dash_core_components as dcc
import dash_html_components as html

from src.db.raw.config import db
from src.db.raw.create import *

def construct_table_row(info):
    players = [ 
                html.Td( children = [
                          html.A(
                                  player.name, 
                                  href = f"player/{player.id}"
                                )
                                    ]
                       )
                for player in info.players
              ]

    return html.Tr( 
            children = [
                            html.Td(info.release_string),
                            html.Td(info.category),
                            html.Td(str(info.date)),
                            html.Td(info.map_name),
                            html.Td(info.time_in_minutes()),
                            *players,
                            html.Td( children = [
                                html.A(
                                        'view', 
                                        href = f"replay/{info.__id__}"
                                      )
                                                ]
                                   )
                       ]
                  )

def construct_table_head():
    return html.Thead( 
                       children = [
                                    html.Th('Build'),
                                    html.Th('Type'),
                                    html.Th('Date'),
                                    html.Th('Map'),
                                    html.Th('Time'),
                                    html.Th('Player One'),
                                    html.Th('Player Two'),
                                    html.Th('View')
                                  ]
                     )

def construct_table_body(query_info):
    return html.Tbody( 
                       children = [
                                    construct_table_row(info)
                                    for info
                                    in query_info
                                  ]
                     )

def construct_replay_table():
    query_info = db.session.query(INFO).all()
    return html.Table(
                        children = [
                                        construct_table_head(),
                                        construct_table_body(query_info)
                                   ],
                     )

