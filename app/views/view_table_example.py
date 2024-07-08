from dash import register_page
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

from app.views.components import rich_card_factory
from app.views.components import data_table_factory


register_page(__name__, path_template='/TableExample', name='データ分析システム-MD確認')


data = dict(
    [
        ("Region", [
            "/",
            "https://en.wikipedia.org/wiki/Toronto",
            "https://en.wikipedia.org/wiki/New_York",
            "https://en.wikipedia.org/wiki/Miami",
            "https://en.wikipedia.org/wiki/San_Francisco",
            "https://en.wikipedia.org/wiki/London",
        ]),
        ("Region", [
            "Montreal",
            "Toronto",
            "New York City",
            "Miami",
            "San Francisco",
            "London",
        ]),
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name"), html.Th('検索', style={'width': '120px'})]))
]

row1 = html.Tr([
    html.Td("Arthur"),
    html.Td("Dent"),
    html.Td(dbc.Button('検索', class_name='py-0 px-2', style={'height': 30}, href='/'), style={'text-align': 'center'})
])

row2 = html.Tr([
    html.Td("Arthur"),
    html.Td("Dent"),
    html.Td(dbc.Button('検索', class_name='py-0 px-2', style={'height': 30}, href='/'), style={'text-align': 'center'})
])

row3 = html.Tr([
    html.Td("Arthur"),
    html.Td("Dent"),
    html.Td(dbc.Button('検索', class_name='py-0 px-2', style={'height': 30}, href='/'), style={'text-align': 'center'})
])

table_body = [html.Tbody([row1, row2, row3])]

df = pd.DataFrame(data)


def layout():
    tbl = data_table_factory(df)
    return dbc.Container([
        dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True)
    ], fluid=True)