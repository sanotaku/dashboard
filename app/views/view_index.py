from dash import html
from dash import register_page
import dash_bootstrap_components as dbc

from app.views.components import rich_label_factory
from app.views.components import rich_card_factory
from app.views.components import gridless_table


register_page(__name__, path_template='/', name='データ分析システム')

labels = ['DeviceName', 'Type', 'URL']
texts = ['MAC-1', 'MAC', 'example.com']
links = [None, None, '/Search']


def layout():
    return dbc.Container([
        dbc.Row([html.H1('Hone Page')]),
        dbc.Row([
            dbc.Col([rich_card_factory([
                rich_label_factory('LotNo', '123ABC123'),
                gridless_table(labels, texts, links)
            ])], width=6)
        ])
    ], fluid=True)
