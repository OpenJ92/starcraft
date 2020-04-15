import dash_core_components as dcc
import dash_html_components as html

def construct_table_row(info):
    return html.Tr( 
            children = [
                            html.Td(str(info.date)),
                            html.Td(info.map_name),
                            html.Td(info.time_in_minutes),
                            html.Td( children = [
                                html.A(
                                        info.players[0].name, 
                                        info.players[0].__id__
                                      )
                                                ]
                                   ),
                            html.Td( children = [
                                html.A(
                                        info.players[1].name, 
                                        info.players[1].__id__
                                      )
                                                ]
                                   ),
                            html.Td( children = [
                                html.A(
                                        'view', 
                                        info.__id__
                                      )
                                                ]
                                   )
                       ]
                  )

def construct_table_head():
    return html.Thead( 
                       children = [
                                    html.Th('Date'),
                                    html.Th('Map'),
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

def construct_replay_table(query_info):
    return html.Table(
                        children = [
                                        construct_table_head(),
                                        construct_table_body(query_info)
                                   ]

                     )

if __name__ == '__main__':
    from src.db.raw.config import db
    from src.db.raw.create import *
