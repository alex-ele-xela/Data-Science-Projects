from dash import Dash, html
import dash_bootstrap_components as dbc

from . import input_box, dashboard


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            dbc.Row([
                dbc.Col(html.H1(app.title)),
                dbc.Col(input_box.render(app))
            ]),
            html.Hr(),
            dashboard.render(app)
        ],
    )
