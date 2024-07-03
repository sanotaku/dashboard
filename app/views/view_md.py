from dash import register_page
import dash_bootstrap_components as dbc
import pandas as pd

from app.views.components import rich_card_factory
from app.views.components import data_table_factory


register_page(__name__, path_template='/MD', name='データ分析システム-MD確認')


data = dict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", [
            "[Montreal](/)",
            "[Toronto](https://en.wikipedia.org/wiki/Toronto)",
            "[New York City](https://en.wikipedia.org/wiki/New_York)",
            "[Miami](https://en.wikipedia.org/wiki/Miami)",
            "[San Francisco](https://en.wikipedia.org/wiki/San_Francisco)",
            "[London](https://en.wikipedia.org/wiki/London)",
        ]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)
df = pd.DataFrame(data)


def layout():
    tbl = data_table_factory(df)
    return dbc.Container([rich_card_factory(tbl)], fluid=True)
