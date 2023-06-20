from dash import Dash, dcc

from . import ids

def render(app: Dash) -> dcc.Dropdown:
    order = [("Highest", False), ("Lowest", True)]

    return dcc.Dropdown(
                id=ids.SORT_DROPDOWN,
                options=[{"label": name, "value": asc} for name, asc in order],
                value=False,
            )
