from dash import html
from dash import register_page
from dash import callback
from dash import dash_table
from dash import Input
from dash import Output
from dash import State
import dash_bootstrap_components as dbc

import pandas as pd
from sklearn.datasets import load_iris

from app.views.components import data_table_factory


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
    df = read_data()
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    [data_table_factory(df)],
                    class_name='m-2 p-2'
                )
            ], width=12)
        ])
    ], fluid=True, class_name='m-2')




