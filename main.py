from dash import Dash
from dash import Input
from dash import Output
from dash import State
from dash import html
from dash import page_container
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import MATCH


app = Dash(__name__, use_pages=True, pages_folder='./app/views', assets_folder='./app/assets', external_stylesheets=[dbc.themes.CERULEAN, dbc.icons.BOOTSTRAP])


def genearte_button(button_name: str, ib_icon: str, url_link: str) -> dbc.ListGroupItem:
    print('OK')
    return dbc.ListGroupItem([
        dbc.NavLink([
            html.I(className=f'{ib_icon} le-0 h5', style={'text-align': 'left', 'margin': '0 0', 'padding': '0 0'}),
            html.P(button_name, style={'text-align': 'left', 'margin': '0 auto 0 10px', 'padding': '0 auto 0 0'}, className='clearfix')
        ], style={'display': 'flex'}),
    ], href=url_link)


navbar = dbc.Container(
    dbc.Navbar(
        children=[
            dbc.Container(children=[
                dbc.Row([
                    dbc.Col(dbc.Button(children=[html.I(className="bi bi-list le-0 h3")], id='show-sidebar', style={'border': '1px solid #333'}), width="auto", align="center"),
                    dbc.Col(dbc.NavbarBrand(children=['データ分析システム'], className="ms-2", style={'color': 'secondary'})),
                ], align="center"),
            ]),
        ],
        color='primary', dark=True,
    )
)

sidebar = dbc.Offcanvas(
    dbc.Container(
        dbc.ListGroup([
            genearte_button('ホーム', 'bi bi-house', '/'),
            genearte_button('検索', 'bi-search', '/Search'),
            dbc.ListGroupItem('BBB'),
        ]), fluid=True, class_name='mx-0 px-0'
    ), is_open=False, id='sidebar', style={'width': 300, 'margin': 0, 'padding': 0}
)


content = page_container


app.layout = dbc.Container([
    dcc.Location(id='my-location'),
    dbc.Row([
        navbar, sidebar,
        dbc.Col(content, width=12, md=6),
    ])
    ], fluid=True, class_name='mx-0 px-0'
)


@app.callback(
    Output("sidebar", "is_open"),
    Input("show-sidebar", "n_clicks"),
    Input("my-location", "pathname"),
    [State("sidebar", "is_open")]
)
def toggle_offcanvas(i1, _, is_open):
    if i1:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server()
