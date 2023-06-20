from dash import Dash, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from . import bar_chart, criteria_dropdown, sort_dropdown, ids, video_stats


def render(app: Dash, videos) -> html.Div:
    @app.callback(
        Output(ids.VIDEO_STATS, 'children'),
        [Input(ids.BAR_CHART, 'clickData')])
    def get_click_title(clickData):
        title = clickData["points"][0]["label"]
        return video_stats.render(app, videos, title)

    return html.Div(
        id=ids.RANKER,
        children=[
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.H4("Videos ranked by :")),
                        dbc.Col(criteria_dropdown.render(app)),
                        dbc.Col(html.H4("Sort by :")),
                        dbc.Col(sort_dropdown.render(app))
                    ]),
                    dbc.Row(bar_chart.render(app, videos))
                ], width=7),
                dbc.Col(
                    id=ids.VIDEO_STATS,
                    children=video_stats.render(app, videos, videos.loc[0].Title)
                )
            ])
        ]
    )
