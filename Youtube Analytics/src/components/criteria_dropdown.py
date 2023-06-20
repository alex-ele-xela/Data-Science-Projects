from dash import Dash, dcc

from . import ids

def render(app: Dash) -> dcc.Dropdown:
    criteria = ["Views", "Likes", "Comments"]

    return dcc.Dropdown(
                id=ids.CRITERIA_DROPDOWN,
                options=[{"label": crit, "value": crit} for crit in criteria],
                value=criteria[0],
            )
