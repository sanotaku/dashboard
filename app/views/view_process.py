from dash import html
from dash import register_page
from sklearn.datasets import load_iris
import dash_bootstrap_components as dbc
import pandas as pd


register_page(__name__, path_template='/Process', name='データ分析システム-工程状況')


def read_data() -> pd.DataFrame:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    targets = []
    for t in iris.target:
        targets.append(iris.target_names[t])
    df['target'] = targets
    return df


def layout():
    return dbc.Container([
        html.H3('Process')
    ], fluid=True)
