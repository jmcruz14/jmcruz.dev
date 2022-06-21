# Dash Imports
import dash
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate

# For Reading Received Data
import base64
import pandas as pd
import io
from itertools import repeat

# for benchmarking purposes
from datetime import time

import sys
sys.path.append('.')
sys.path.append('..')

# App Files
from app import app

# parse_contents - show Address only - important for the table
def parse_contents(contents, filename, date):
    if contents is not None:

        content_type, content_string = contents.split(',') # should produce 'data:text/csv;base64, 77u/...'
                                                            # Enabled by setting multiple = True in portal_page file

        # content_type "data:text/csv;base64"
        # content_string "77u/QWRkcmVzcw0KIkx1eHVy"

        decoded = base64.b64decode(content_string)

        try: 
            if 'csv' in filename:
                # Assume CSV file was uploaded
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            elif 'xlsx' in filename:
                # Excel file - xlsx
                df = pd.read_excel(io.BytesIO(decoded))
            elif 'xls' in filename:
                # Excel file - xls
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div(
                [
                    'There was an error processing this file.'
                ])

        df = df['Address'].to_frame()
        df.dropna(how='any', inplace=True)

        if len(df) > 15:

            return  dbc.Alert(
                children = 'Too many addresses. This application only accepts 15 at most.', 
                color='warning', 
                id='address_count_alert',
                fade = True, 
                duration = 1500, 
                is_open=True)

        else:
        
            data_table = dash_table.DataTable(
                df.to_dict('records'),
                [{'name': i, 'id': i} for i in df.columns], 
                page_action='none',
                style_table={'height': '210px', 'overflowY': 'auto'},
                style_cell={'fontFamily': "Trebuchet MS"},
            )
            
            return data_table
    else:
        raise PreventUpdate

# parse_contents – retrieve entire info
def parse_contents_full(contents, filename, date):
    if contents is not None:

        content_type, content_string = contents.split(',') # should produce 'data:text/csv;base64, 77u/...'
                                                            # Enabled by setting multiple = True in portal_page file

        # content_type "data:text/csv;base64"
        # content_string "77u/QWRkcmVzcw0KIkx1eHVy"

        decoded = base64.b64decode(content_string)

        try: 
            if 'csv' in filename:
                # Assume CSV file was uploaded
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            elif 'xlsx' in filename:
                # Excel file - xlsx
                df = pd.read_excel(io.BytesIO(decoded))
            elif 'xls' in filename:
                # Excel file - xls
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div(
                [
                    'There was an error processing this file.'
                ])

        df.dropna(how='any', inplace=True) # This function is to ensure that the program will only read FULLY ENCODED DATA (missing rows / columns not allowed)

        df = df.to_dict()

        print(df)

        return df

    else:
        raise PreventUpdate

# Read CSV file
@app.callback(
    [
        Output('output_data_upload', 'children'),
        Output('file_status', 'children'),
        Output('address_session', 'data')
    ],
    [  
        Input('upload_data', 'contents')
    ],
    [
        State('upload_data', 'filename'),
        State('upload_data', 'last_modified')
    ]
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, repeat(list_of_dates))]
        full_df = [parse_contents_full(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, repeat(list_of_dates))]

        return [children, list_of_names, full_df]
    else:
        raise PreventUpdate