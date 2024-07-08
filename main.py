from dash import Dash
from dash import Input
from dash import Output
from dash import State
from dash import dcc
from dash import html
from dash import page_container
import dash_bootstrap_components as dbc


app = Dash(
    __name__,
    use_pages=True,
    pages_folder='./app/views',
    assets_folder='./app/assets',
    external_stylesheets=[dbc.themes.CERULEAN, dbc.icons.BOOTSTRAP]
)


def genearte_button(button_name: str, ib_icon: str, url_link: str) -> dbc.ListGroupItem:
    return dbc.ListGroupItem([
        dbc.NavLink([
            html.I(className=f'{ib_icon} le-0 h5', style={'text-align': 'left', 'margin': '0'}),
            html.P(button_name, style={'margin': '0 auto 0 10px'})
        ], style={'display': 'flex'}),
    ], href=url_link)


sidebar = dbc.Offcanvas(
    dbc.Container(
        dbc.ListGroup([
            genearte_button('ホーム', 'bi bi-house', '/'),
            genearte_button('検索', 'bi-search', '/Search'),
            genearte_button('MD確認', 'bi-filetype-md', '/MD'),
            genearte_button('工程状況', 'bi bi-bar-chart-steps', '/Process'),
            genearte_button('テーブル', 'bi bi-bar-chart-steps', '/TableExample'),
        ]), fluid=True, class_name='mx-0 px-0'
    ), is_open=False, id='sidebar', style={'width': 300, 'margin': 0, 'padding': 0}
)


navbar = dbc.Container(
    dbc.Navbar(
        children=[
            dbc.Container(children=[
                dbc.Row([
                    dbc.Col(dbc.Button(children=[html.I(className="bi bi-list le-0 h3")], id='show-sidebar', style={'border': '1px solid', 'border-color': 'secondary'})),
                    dbc.Col(dbc.NavbarBrand(children=['データ分析システム'], className="ms-2", style={'color': 'secondary'}, href='/')),
                ], align="center")
            ], fluid=True),
        ],
        color='primary', dark=True, fixed='top', style={'box-shadow': '0px 1px 2px'}
    )
)


content = page_container


app.layout = dbc.Container([
    dcc.Location(id='my-location'),
    dbc.Row([
        sidebar, navbar,
        dbc.Col(content, width=12, style={'margin-top': '70px'}),
    ])
    ], fluid=True, class_name='mx-0 px-0'
)


@app.callback(
    Output("sidebar", "is_open"),
    Input("show-sidebar", "n_clicks"),
    Input("my-location", "pathname"),
    [State("sidebar", "is_open")],
    prevent_initial_call=False
)
def toggle_sidebar(i1, _, is_open):
    if i1:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server()
