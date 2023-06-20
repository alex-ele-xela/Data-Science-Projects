import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def get_bar_chart(videos, criteria, asc):
    top10videos = videos.sort_values(by=criteria, ascending=asc).head(10)

    fig = px.bar(top10videos, x=criteria, y="Title")
    fig.update_layout(clickmode='event+select')
    fig.update_layout(yaxis = {"categoryorder":"total ascending"})

    return fig


def render(app: Dash, videos) -> dcc.Graph:
    @app.callback(
        Output(ids.BAR_CHART, "figure"),
        [Input(ids.CRITERIA_DROPDOWN, "value"),
         Input(ids.SORT_DROPDOWN, "value")]
    )
    def update_bar_chart(criteria, asc) :
        return get_bar_chart(videos, criteria, asc)

    return dcc.Graph(
                id=ids.BAR_CHART,
                figure=get_bar_chart(videos, "Views", False)
        )