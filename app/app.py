import webbrowser
from multiprocessing import freeze_support
import logging
import matplotlib

from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from layout.navbar import navbar
from layout.display import display
from callbacks import load_all
import config
from dash_app import app

load_figure_template('LITERA')

matplotlib.use(backend='Agg')

app.layout = html.Div(dbc.Container(fluid=True, children=[
    dbc.Row([
        navbar.navbar,
        display.display,
    ]),
]))

if __name__ == '__main__':
    if config.bundled_mode:
        freeze_support()
        webbrowser.open('http://127.0.0.1:8050')

    # Hide the noisy internal Docker IP logs
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    print("App running at: http://127.0.0.1:8050")

    app.run_server(
        debug=config.debug_mode,
        host='0.0.0.0',
        port=8050,
        dev_tools_silence_routes_logging=True  # <- hides "Dash is running on..."
    )