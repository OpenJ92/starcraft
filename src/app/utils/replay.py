import dash_core_components as dcc
import dash_html_components as html

from src.db.raw.config import db
from src.db.raw.create import *

def construct_table_row(info):
    teams = {}
    for player in info.players:
        if player.team_id not in teams.keys():
            teams[player.team_id] = [player]
        else:
            teams[player.team_id].append(player)

    players = [ 
                html.Td( children = [
                                *[
                                    html.Div(
                                                html.A(
                                                        player.name, 
                                                        href = f"player/{player.id}"
                                                      )
                                            )
                                    for player in players
                                 ]
                                    ]
                       )
                for team, players in teams.items()
              ]

    return html.Tr( 
            children = [
                            html.Td(info.release_string),
                            html.Td(info.type),
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
                                    html.Th('Team One'),
                                    html.Th('Team Two'),
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

