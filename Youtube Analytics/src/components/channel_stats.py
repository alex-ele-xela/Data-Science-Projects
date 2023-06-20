from dash import Dash, html
import dash_bootstrap_components as dbc

from . import ids


def render(app: Dash, stats: dict) -> html.Div:
    return html.Div(
        id=ids.CHANNEL_STATS,
        children=[
            dbc.Row([
                dbc.Col(html.Img(
                    src=stats['Thumbnail'],
                    alt="Channel Thumbnail"
                ), width=3),

                dbc.Col(html.H2(stats["ChannelName"]), width=3),
                
                dbc.Col([
                    dbc.Row(html.H3(f"{stats['Subscribers']:,}")),
                    dbc.Row(html.P("subscribers"))
                ], width=2),

                dbc.Col([
                    dbc.Row(html.H3(f"{stats['Views']:,}")),
                    dbc.Row(html.P("views"))
                ], width=2),

                dbc.Col([
                    dbc.Row(html.H3(f"{stats['Videos']:,}")),
                    dbc.Row(html.P("videos"))
                ], width=2)
            ])
        ]
    )
