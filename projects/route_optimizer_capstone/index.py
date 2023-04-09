## Modules
import time
import requests

# Dash Imports
import dash
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate

# Route Optimization
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
solver = pywrapcp.Solver("CPSimple")

# Web Browsing and Datetime
import webbrowser

# Geospatial Analysis
import networkx as nx
import pandas as pd
import geocoder

# App Files
from app import app
import apps.dbconnect as db
from apps import portal_page
from apps import login_page

# Function Files
from functions import read_excel
from functions import load_navbar
from functions import save_pdf

# Hashing for Password Encryption
import hashlib
import base64
from requests_oauthlib import OAuth2Session
import random
import string

 
# API KEY (Google)
API_KEY = API_KEY_GOOGLE

# Base URL (Google Geocoder)
base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# API KEY (Mapquest)
API_KEY_MQ = API_KEY_MAPQUEST

# Base URL (Mapquest Optimized Route)
base_url_mq = 'http://www.mapquestapi.com/directions/v2/optimizedroute?key={key}&json={bracket}{locations}: {coordinates}{bracket_b}'

## Developer's note: These API keys are currently registered under my personal account. Please refer to the video guide to find out
# how to create your own API Key to replace my API Keys.

server = app.server

## General layout
app.layout = html.Div(
    [
        # Url 
        dcc.Location(id='url', refresh=True),
        
        # Site Content
        html.Div(id='navbar'),
        html.Div(id='page_content'),
    ]
)

## Functions

# new global optimal distance calculation
def distance_within_all_coordinates(*args):
    args = args[0]

    print(args)

    response = requests.get(base_url_mq.format(key=API_KEY_MQ, bracket="{", locations="locations", coordinates=args, bracket_b="}")).json()
    location_sequence = response["route"]["locationSequence"]
    locations = response["route"]["locations"]

    distance = response["route"]["distance"] # √

    print('location sequence', location_sequence)
    print('distance', distance * 1.609344, 'kilometers')

    return response

#%% 

## Callbacks

# Initiate Optimization
@app.callback(
    [
        Output('address_points', 'data'),
        Output('upload_alert', 'color'),
        Output('upload_alert', 'children'),
        Output('upload_alert', 'is_open'),
        Output('results_optimization', 'children'),
        Output('cluster_name_1', 'data')
    ],
    [
        Input('submit_addresses', 'n_clicks')
    ],
    [
        State('output_data_upload', 'children'),
        State('cluster_dropdown', 'value'),
        State('first_loc_toggle', 'value')
    ]
)
def begin_optimizing(submitbtn, addresses, cluster, toggle):
    ctx = dash.callback_context
    if ctx.triggered:
        if addresses:
            if cluster:
                start_time = time.monotonic()

                eventid = ctx.triggered[0]['prop_id'].split('.')[0]
                if eventid == 'submit_addresses' and submitbtn:

                    # Initialize lists for MapQuest to Optimize
                    list_of_addresses = addresses[0]['props']['data']

                    address_names = [x['Address'] for x in list_of_addresses]
                    address_names_updated = list(map(lambda x : x if cluster in x else x + ', {}'.format(cluster), address_names))

                    if toggle != True:
                        address_index = list(range(len(list_of_addresses) + 1))
                    else:
                        address_index = list(range(len(list_of_addresses)))

                    # if toggle != True:
                    #     address_names_updated.insert(0, 'HQ')
                    # else:
                    #     pass

                    match_address = dict(zip(address_index, address_names_updated))

                    address_dict = []
                    #distance_data = []
                    location_data = []
                    distance_matrix = []

                    # if checkbox is not set to start at first address
                    # if toggle != True:
                    #     address_dict.append(
                    #         dict(
                    #             lat=0, 
                    #             lon=0
                    #         )
                    #     )

                    # Employ Google Geocoder API
                    for address in list_of_addresses:

                        ### Use of the Google Maps API Key is limited to a certain number of requests beyond which payment must be acquired.

                        # Initialize parameters
                        params = {
                            'key': API_KEY,
                            'address': address['Address']
                        }

                        # Request for Address
                        response = requests.get(base_url, params=params).json()

                        if response['status'] == 'OK':

                            geometry = response['results'][0]['geometry']

                            address_dict.append(
                                dict(
                                    lat = geometry['location']['lat'],
                                    lon = geometry['location']['lng']
                                )
                            )
                        
                        else: # Back-up plan in case the Google Geocoder does not work

                            address_dict.append(
                                dict(
                                    lat=geocoder.osm(address).lat if geocoder.osm(str(address)).lat is not None else (geocoder.mapquest(str(address), key='jzKWwxm0O7mYNhnuuFwKqeyv9G0A86a8').lat),
                                    lon=geocoder.osm(address).lng if geocoder.osm(str(address)).lng is not None else (geocoder.mapquest(str(address), key='jzKWwxm0O7mYNhnuuFwKqeyv9G0A86a8').lng)
                                )
                            )

                    # Generates points to be reflected on the map to the left
                    geojson = dlx.dicts_to_geojson([{**c} for c in address_dict]) # Developer's note: The Dash Leaflet documentation could be studied to 
                    # explore how to include "name" labels on the map

                    for address in address_dict:
                        location_data.append('{},{}'.format(address['lat'], address['lon']))

                    # Gather Optimal Distance via MapQuest
                    response = distance_within_all_coordinates(location_data)

                    if response['info']['statuscode'] == 0:

                        route_list = response["route"]["locationSequence"]  
                        total_distance = response["route"]["distance"]

                        total_distance = total_distance * 1.609344 # CONVERT MILES TO KILOMETERS

                        df = pd.DataFrame({"Order": route_list})
                        df['Order'] = df['Order'].apply(lambda x: match_address[int(x)])

                        # Feed df into another data store which will be used to CONCATENATE FOR EXCEL FILE
                        # df["Address"] = df 

                        process_time = time.monotonic() - start_time

                        result_table = html.Div(
                            [
                                html.H2("Optimized Route", style={'marginLeft': '10px', 'paddingTop': '4px', 'backgroundColor': '#3e444a', 'color': '#FFFFFF'}),
                                html.Div(
                                    dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, class_name='table-dark table-striped', id='optimized_results'), 
                                    style={"maxHeight": "365px", "overflow": "scroll"}
                                    ),
                                html.Div(
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [html.H4("Process Time:", style={'marginLeft': '17px', 'marginTop': '3px', 'marginBottom': '0px', 'color': '#FFFFFF'}),
                                                html.P(
                                                    "{:.2f} seconds".format(process_time), 
                                                    style={'marginLeft': '17px', 'marginTop': '4px', 'paddingBottom': '4px', 'paddingTop': '2.5px', 'color': '#cccccc'}
                                                    )]
                                                ),
                                            dbc.Col([html.H4("Total Distance:", style={'marginLeft': '17px', 'marginTop': '3px', 'marginBottom': '0px', 'color': '#FFFFFF'}),
                                            html.P("{:.2f} kilometers".format(total_distance), style={'marginLeft': '17px', 'marginTop': '4px', 'paddingBottom': '25px', 'paddingTop': '2.5px', 'color': '#cccccc'})]),
                                        ],
                                        style = {'marginLeft': 'auto', 'marginTop': '10px', "overflow": "auto", 'marginBottom': '-4px'}
                                    ),
                                style = {"overflow": "auto"}
                                )
                            ],
                            style = {'backgroundColor': '#3e444a', "overflow": "auto"}
                        )

                        no_update = dash.no_update

                        return [geojson, no_update, no_update, no_update, result_table, cluster]

                    else:
                        result_alert = dbc.Alert('No feasible solution could be found. Review the integrity of your submitted addresses.', color='danger')
                        no_update = dash.no_update

                        return [no_update, no_update, no_update, no_update, result_alert, no_update] 
            else:
                no_update = dash.no_update
                submit_alert_color = 'warning'
                submit_alert_text = 'Please select a corresponding cluster!'
                submit_alert_open = True

                return [no_update, submit_alert_color, submit_alert_text, submit_alert_open, no_update, no_update]

        else:
            no_update = dash.no_update
            submit_alert_color = 'warning'
            submit_alert_text = 'Upload an appropriate CSV or Excel file first!'
            submit_alert_open = True
            
            return [no_update, submit_alert_color, submit_alert_text, submit_alert_open, no_update, no_update]
    else:
        raise PreventUpdate

if __name__ == '__main__':

    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)

    app.run_server(debug=False)