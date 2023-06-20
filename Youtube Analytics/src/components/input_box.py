from dash import Dash, dcc, html

from . import ids


def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            dcc.Input(
                id=ids.INPUT_TEXT_BOX,
                placeholder='Enter input here...', 
                value="UCiT9RITQ9PW6BhXK0y2jaeg",
                type='text',
                debounce=True,
                size=30
            ),
            # html.Button(
            #     children=["Show Stats"],
            #     id=ids.INPUT_TEXT_BUTTON,
            #     n_clicks=0,
            # ),
        ]
    )