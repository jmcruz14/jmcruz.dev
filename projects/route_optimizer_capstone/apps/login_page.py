# Dash Imports
import dash
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate

import sys
sys.path.append('.')
sys.path.append('..')

# App Files
from app import app
from apps import portal_page
import apps.dbconnect as db

# Password Authentication
import hashlib
from datetime import datetime
import pandas as pd
import numpy as np
import base64
from requests_oauthlib import OAuth2Session
import random
import string

CONTENT_STYLE = {
    "margin-left": "auto",
    "margin-right": "auto",
    "padding": "2rem 2rem",
    "display": "flex"
}

layout = html.Div(
    [
        dbc.Col(
            [
            dbc.Row(dbc.Carousel(
                    items = [
                        {
                            "key": "1",
                            "src": app.get_asset_url('login_page_tutorial.png'),
                            "caption": "Tutorial Window"
                        }
                    ]
                )),
            html.Br(),
            dbc.Row(
                html.P("""Shown in the portal page in order: \n(1) Upload Box \n(2) First Address Toggle \n(3) Submit Address Button \n(4) File status
                \n(5) Cluster Dropdown Menu \n(6) Addresses for Processing \n(7) Interactive Map \n(8) Optimized Route \n(9) Process Time \n(10) Total Distance\n
                (11) Excel Download Button \n(12) PDF Download Button"""))
            ]
        ),
        
        dbc.Col(dbc.Container(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            html.H4("Log-in Window")
                        ),

                        dbc.CardBody(
                            [
                                dbc.Row(
                                    [
                                        html.H4("Username"),
                                        dbc.Input(id='login_username', type='text'),  
                                    ],
                                    style = {'paddingLeft': '10px', 'paddingRight': '10px'}
                                ),

                                html.Br(),

                                dbc.Row(
                                    [
                                        html.H4("Password"),
                                        dbc.Input(id='login_password', type='password')
                                    ],
                                    style = {'paddingLeft': '10px', 'paddingRight': '10px'}
                                )
                                
                                
                            ]
                        ),

                        dbc.CardFooter(
                            dbc.Row(
                                [
                                    dbc.Button("Submit", id='submit_login_info', n_clicks=0),
                                ]
                            )
                        ),

                        dbc.Alert(id='successful_login_alert', is_open=False, fade=True)
                    ]
                )
            ]
        )),
    ],
    style = CONTENT_STYLE
)

# Function for Password Hashing
def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

# Callback
# Login User
@app.callback(
    [
        Output('successful_login_alert', 'is_open'),
        Output('successful_login_alert', 'color'),
        Output('successful_login_alert', 'children'),
        Output('url', 'pathname')
    ],
    [
        Input('submit_login_info', 'n_clicks')
    ],
    [
        State('login_username', 'value'),
        State('login_password', 'value')
    ]
)
def login_user(submitbtn, username, password):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]

        if eventid == 'submit_login_info' and submitbtn:

            if username and password:
                
                # Check SQL
                sql = """
                SELECT login_id, login_uname, login_pass from login_details
                WHERE login_uname = %s
                AND login_pass = %s
                AND login_del_ind = %s"""

                values = [username, password, False]

                cols = ['ID', 'Username', 'Password']

                df = db.querydatafromdatabase(sql, values, cols)

                if df.shape[0] == 1:
                    alert_open = True
                    alert_color = 'success'
                    alert_text = 'Successful log-in!'
                    output_url = '/main_portal'

                    return [alert_open, alert_color, alert_text, output_url]

                else:
                    alert_open = True
                    alert_color = 'danger'
                    alert_text = 'Please enter the correct credentials.'
                    output_url = dash.no_update

                    return [alert_open, alert_color, alert_text, output_url]
            
            else:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please input your login credentials.'
                output_url = dash.no_update

                return [alert_open, alert_color, alert_text, output_url]
            
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate