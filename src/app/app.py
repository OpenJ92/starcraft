import dash
import dash_core_components as dcc
import dash_html_components as html

from src.db.raw.config import server, db

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
                    __name__, 
                    server = server, 
                    external_stylesheets=external_stylesheets
               )
app.config.suppress_callback_exceptions = True
