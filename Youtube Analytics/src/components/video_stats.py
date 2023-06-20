from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import json

from . import ids, video_embed


def render(app: Dash, videos, title) -> list[dbc.Row]:
    details = videos[videos["Title"]==title]

    return [
            dbc.Row(video_embed.render(app, details.ID.values[0], title)),
            dbc.Row(html.H4(title)),
            dbc.Row([                        
                dbc.Col([
                    dbc.Row(html.H5(f"{details.Views.values[0]:,}")),
                    dbc.Row(html.P("views"))
                ], width=4),

                dbc.Col([
                    dbc.Row(html.H5(f"{details.Likes.values[0]:,}")),
                    dbc.Row(html.P("likes"))
                ], width=4),

                dbc.Col([
                    dbc.Row(html.H5(f"{details.Comments.values[0]:,}")),
                    dbc.Row(html.P("comments"))
                ], width=4)
            ])
        ]
