from dash import Dash, html

from . import ids


def render(app: Dash, id, title) -> html.Div:

    return html.Iframe(
                id=ids.VIDEO_EMBED,
                # width="100%",
                height=350,
                src=f"https://www.youtube.com/embed/{id}",
                title=title,
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        )

