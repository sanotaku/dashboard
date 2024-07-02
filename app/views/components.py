import pandas as pd
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc


def data_table_factory(df: pd.DataFrame) -> html.Div:
    return dbc.Container(
        dbc.Row([
            dbc.Col([icon_and_button('CSV出力', 'bi bi-filetype-csv', 'search-csv-button')], class_name='my-1', style={'text-align': 'right'}),
            dbc.Col([dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])], width=12),
        ]),
    )


def icon_and_button(button_name: str, ib_icon: str, id_name: str) -> dbc.Button:
    return dbc.Button([
        html.I(className=f'{ib_icon} le-0 h5', style={'text-align': 'left', 'margin': '0', 'color': 'white'}),
        html.P(button_name, style={'margin': '0 auto 0 10px'})
    ], style={'display': 'flex'}, id=id_name)

