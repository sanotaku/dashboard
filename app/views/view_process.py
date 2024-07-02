from dash import html
from dash import register_page
import dash_bootstrap_components as dbc


register_page(__name__, path_template='/Process')


def layout():
    return dbc.Container([html.H1('Process')])
