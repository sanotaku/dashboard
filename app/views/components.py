from typing import Optional

from dash import dash_table
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd


def data_table_factory(df: pd.DataFrame, height: int=300) -> dbc.Container:
    return dbc.Container(
        dbc.Row([
            dbc.Col(
                class_name='my-1', style={'text-align': 'right'}, width=12,
            ),
            dbc.Col(
                children=[
                    dash_table.DataTable(
                        data=df.to_dict('records'),
                        columns=[{'id': c, 'name': c,  'presentation': 'markdown'} for c in df.columns],
                        css=[{"selector": "p", "rule": "margin: 0"}],
                        export_format='csv',
                        style_table={'height': f'{height}px', 'overflowY': 'auto', 'border': '1px solid #CCC'}
                    )
                ],
                width=12),
        ]), fluid=True
    )


def icon_and_button_factory(button_name: str, ib_icon: str, id_name: str) -> dbc.Button:
    return dbc.Button([
        html.I(className=f'{ib_icon} le-0 h5', style={'text-align': 'left', 'margin': '0', 'color': 'white'}),
        html.P(button_name, style={'margin': '0 auto 0 10px'})
    ], style={'display': 'flex'}, id=id_name)


def rich_label_factory(
        title: str,
        text: str,
        id_name: str='',
        color: str='secondary',
        bg_color: str='primary',
        width: int=200) -> dbc.Card:
    return dbc.Card(
        dbc.Container([
            dbc.Row(dbc.Col([html.H6(title, style={'color': color, 'font-size': '1em', 'margin-bottom': 0})])),
            dbc.Row(dbc.Col([html.H4(text, style={'color': color, 'margin-bottom': 0})]))
        ]), id=id_name, color=bg_color, class_name='py-2', style={'width': f'{width}px'})


def rich_card_factory(children: list, id_name=None) -> dbc.Card:
    if id_name:
        return dbc.Card(children, class_name='m-2 p-2', style={'box-shadow': '1px 1px 4px'}, id=id_name)
    else:
        return dbc.Card(children, class_name='m-2 p-2', style={'box-shadow': '1px 1px 4px'})


def gridless_table(labels: list, texts: list, links: Optional[list]=None) -> dbc.Container:
    if len(labels) != len(texts):
        raise ValueError()
    
    if links is None:
        links = [None for _ in range(len(labels))]

    body = []

    max_len = 0
    for label in labels:
        if max_len < len(label):
            max_len = len(label)

    for label, text, link in zip(labels, texts, links):

        if link == '' or link is None:
            text_element = html.P(text, style={'font-size': '1em', 'margin-left': '50px'})
        else:
            text_element = html.A(html.P(text, style={'font-size': '1em', 'margin-left': '50px'}), href=link)

        record = html.Div([
            html.P(label, className='p-0 m-0', style={'width': f'{max_len}em', 'color': 'gray', 'font-size': '1em'}),
            text_element
        ], style={'display': 'flex'})

        body.append(record)
        
    return dbc.Container(body, class_name='m-2')
