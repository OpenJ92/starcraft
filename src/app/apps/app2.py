import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.app.app import app

layout = lambda x: html.Div(
    [
        html.H3("App 2"),
        dcc.Dropdown(
            id="app-1-dropdown",
            options=[
                {"label": "App 2 - {}".format(i), "value": i}
                for i in ["NYC", "MTL", "LA", x]
            ],
        ),
        html.Div(id="app-2-display-value"),
        dcc.Link("Go to App 1", href="/apps/app1"),
    ]
)


@app.callback(
    Output("app-2-display-value", "children"), [Input("app-2-dropdown", "value")]
)
def display_value(value):
    return 'You have selected "{}"'.format(value)
