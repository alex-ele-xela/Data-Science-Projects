from dash import Dash, html
from dash.dependencies import Input, Output

from . import channel_stats, ranker, ids
from data.utilities import create_youtube_api, get_channel
from data import constants

def create_dashboard_elements(app, channel_id) -> list:
    youtube = create_youtube_api(
            constants.API_KEY, constants.API_SERVICE_NAME, constants.API_VERSION
        )
    channel = get_channel(youtube, channel_id)

    return [
            channel_stats.render(app, channel.get_stats()),            
            html.Hr(),
            ranker.render(app, channel.get_videos())
        ]

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.DASHBOARD, "children"),
        [Input(ids.INPUT_TEXT_BOX, "value")]
    )
    def update_dashboard(channel_id) -> html.Div:
        return create_dashboard_elements(app, channel_id)

    return html.Div(
        id=ids.DASHBOARD,
        className='dashboard',
        children=create_dashboard_elements(app, "UCiT9RITQ9PW6BhXK0y2jaeg")
    )
