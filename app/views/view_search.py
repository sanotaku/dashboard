from dash import register_page
from dash import callback
from dash import dcc
from dash import Input
from dash import Output
from dash import State
from dash import no_update
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

import pandas as pd
from sklearn.datasets import load_iris

from app.views.components import data_table_factory
from app.views.components import rich_card_factory
from app.views.components import icon_and_button_factory


register_page(__name__, path_template='/Search')


def read_data() -> pd.DataFrame:
    print('load iris')
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    targets = []
    for t in iris.target:
        targets.append(iris.target_names[t])
    df['target'] = targets
    return df


def layout():
    return dbc.Container([
        rich_card_factory([
            dbc.Row([
                dbc.Col(dbc.Input(id='search-keyword', type='text')),
                dbc.Col(icon_and_button_factory('検索', 'bi-search', 'search-submit')),
            ]),
            dbc.Row([
                dbc.Col(id='search-chart', width=12)
            ]),
            dbc.Row([
                dbc.Col(width=12, id='search-datatable')
            ])
        ]),
        dbc.Modal(id='point-detail', is_open=False, size='xl')
    ], fluid=True, class_name='m-2')


@callback(
    Output('search-datatable', 'children'),
    Output('search-chart', 'children'),
    Input('search-submit', 'n_clicks'),
    State('search-keyword', 'value')
)
def search(i1, s1):
    df = read_data()

    if s1 != None:
        df = df[df['target'] == s1]

    fig = make_subplots(rows=1, cols=1)
    fig.append_trace(
        go.Scatter(x=df['sepal length (cm)'], y=df['sepal width (cm)'], mode='markers'), row=1, col=1)

    return data_table_factory(df, 300), dcc.Graph(figure=fig, id='search-graph')


@callback(
    Output('point-detail', 'is_open'),
    Output('point-detail', 'children'),
    Output("search-graph", "clickData"),
    Input('search-graph', 'clickData'),
)
def search_popup(i1):
    if i1 is None:
        return no_update
    
    model = [
        dbc.ModalHeader(dbc.ModalTitle('グラフデータ詳細')),
        dbc.ModalBody(children=[str(i1)]),
    ]

    return True, model, None
