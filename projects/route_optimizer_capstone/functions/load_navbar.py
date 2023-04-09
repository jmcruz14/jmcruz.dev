# Dash Imports
import dash
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate

# App Files
from app import app
import apps.dbconnect as db
from apps import portal_page
from apps import login_page

# Load navbar
@app.callback(
    [
        Output('navbar', 'children'),
        Output('page_content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def load_navbar(pathname):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if pathname == '/':
            navbar = portal_page.portal
            pagecontent = login_page.layout
            
            return [navbar, pagecontent]

        elif pathname == '/main_portal':
            navbar = portal_page.portal
            pagecontent = portal_page.upload_box

            return [navbar, pagecontent]

        else:
            raise PreventUpdate
    else:
        raise PreventUpdate