from dash import html
from dash import register_page
import dash_bootstrap_components as dbc

from app.views.components import rich_label_factory
from app.views.components import rich_card_factory
from app.views.components import gridless_table


register_page(__name__, path_template='/')

labels = ['ポケモン名', 'タイプ', 'H', 'A', 'B', 'C', 'D', 'S', '特性']
texts = ['ニャオハ', 'くさ', 40, 61, 54, 45, 45, 65, 'へんげんじざい']
links = ['/Search', '', None, None, None, None, None, None, None]


def layout():
    return dbc.Container([
        dbc.Row([html.H1('Hone Page')]),
        dbc.Row([
            dbc.Col([rich_card_factory([
                rich_label_factory('LotNo', '123ABC123', 'test-rich-label1'),
                gridless_table(labels, texts, links)
            ])], width=6)
        ])
    ])
