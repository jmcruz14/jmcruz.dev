# Dash Imports
import dash
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate
from dash_extensions.snippets import send_bytes

import sys, os
sys.path.append('.')
sys.path.append('..')

# App Files
from app import app
from apps import portal_page

# Function Files
from functions import save_pdf

# for excel and pdf
import pandas as pd
from fpdf import FPDF


## Map design source
url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'

portal = dbc.Navbar(
    [
        dbc.Container(
            [
                # opted to insert a placeholder mykuya logo, feel free to change this accordingly
                html.H3('Route Optimizer Software', style = {'color': 'white'})
            ],
            fluid = False
        )
    ],
    color = "#1a1a1a",
    style = {'width': '100%'}
)

# Consider relocating this to the index file for easier inline programming
upload_box = html.Div(
    [
        # Alert Button – Upload
        dbc.Alert(id='upload_alert', is_open=False, fade = True, duration = 2000),

        # Store Cluster Data for Excel/PDF upload
        dcc.Store(id="cluster_name_1", storage_type="session"),

        # Upload Box
        dcc.Upload(
            id='upload_data',
            children = html.Div(
                [ 
                    'Drag file here or ',
                    html.B(
                        html.A('Select a File')
                        )
                ]
            ),
            max_size = 16 * 1024 * 1024, # 16 MB max upload size
            style = 
                {
                    'width': 'auto',
                    'height': '60px',
                    'line-height': '40px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
            multiple=True,
        ),

        html.Div(

            dbc.Card(
                dbc.CardBody(

                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Checkbox(
                                            id='first_loc_toggle',
                                            label='  Start at the First Address?',
                                            value = True
                                        ) 
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    html.H4("STATUS:"),
                                                    width=2
                                                ),
                                                
                                                dbc.Col(
                                                    [
                                                        html.H5(id = 'file_status', children="No File Uploaded", style={'fontFamily': 'Avenir', 'marginTop':'4px'})
                                                    ],
                                                    width = 8 
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ],
                            justify = 'around',
                            align = 'center'
                        ),

                        html.Br(),

                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Button('Submit', id='submit_addresses'),
                                    width = 3
                                ),

                                dbc.Col(

                                    dbc.Row(
                                        [
                                            # insert dropdown and label "cluster" here 
                                            dbc.Col(html.H4("Cluster:")),

                                            dbc.Col(
                                                    dcc.Dropdown( # To be used as cluster identifier (to add in address)
                                                    options = [
                                                        {'label': 'Metro Manila', 'value': 'Metro Manila'},
                                                        {'label': 'Rizal', 'value': 'Rizal'},
                                                        {'label': 'Laguna', 'value': 'Laguna'},
                                                        {'label': 'Cavite', 'value': 'Cavite'},
                                                        {'label': 'Bulacan', 'value': 'Bulacan'}
                                                    ],
                                                    id = 'cluster_dropdown',
                                                    searchable = False,
                                                    clearable = True,
                                                    disabled = False
                                                ),
                                                width = 9
                                            ),
                                        ],
                                        className= 'g-0'
                                    ),

                                    width = 5
                                )
                            ],

                            justify = "around",
                        )
                    ]
                )
            ),
            style = {'width': '100%'}
        ),

        # Data Store
        dcc.Store(id='address_sheet_data', storage_type='memory'),

        # Dynamic Output
        html.Div(id='output_data_upload'),

        # Alert Button – Upload
        dbc.Alert(id='download_alert', is_open=False, fade = True, duration = 2000),

        dbc.Row(
            [
                dbc.Col(

                    # Map Layout
                    dbc.Spinner(
                        children = [
                            dl.Map(
                                [
                                    dl.TileLayer(url=url), 
                                    dl.GeoJSON(id='address_points', zoomToBounds=True)
                                ], 
                                center=[14.5452019, 121.0163377], 
                                style={'width': '100%', 'height': '565px'}, 
                                zoom=20,
                                attributionControl=False
                            )
                        ],
                        color = 'primary',
                        fullscreen=False,
                        show_initially = False, 
                        type = None,
                        delay_hide = 500,
                        delay_show = 750, 
                        spinner_class_name='spinner',
                        size = {'width': '20%', 'height': '20%'}
                    ),

                    width = 8
                ),

                dbc.Col(
                    [
                        html.Div(
                        id = 'results_optimization',
                        style = {
                            'height': '517px',
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            'width': 'inherit'
                            }
                        ),

                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Download as Excel File", id='excel_download', n_clicks = 0)),
                                dbc.Col(dbc.Button("Download as PDF", id='pdf_download', n_clicks = 0))
                            ],
                            className = 'g-0'  
                        )
                    ]
                )
            ],
            style = {'borderStyle': 'solid', 'borderWidth': '3.5px', 'backgroundColor': 'rgb(26, 26, 26)'}
        ),

        # Data Stores
        dcc.Store(id="address_session", storage_type="session"), # store here to download as excel file
        dcc.Store(id='optimized_address_data', storage_type="session"), # insert dataframe here

        dcc.Download(id='download_file_xlsx'),
        dcc.Download(id='download_file_pdf'),

        html.Br(),

        html.Br(),

        html.Br(),

        dbc.Modal(
            [
                dbc.ModalHeader(
                    "Download in progress..."
                ),
                dbc.ModalBody(
                    "You may now close this window."
                )
            ],
            id = 'download_window',
            autofocus = True,
            backdrop = True,
            is_open = False
        )
    ],
    hidden = False,
)

# Download as Excel File 
# Download as PDF
@app.callback(
    [
        Output('download_alert', 'color'),
        Output('download_alert', 'children'),
        Output('download_alert', 'is_open'),
        Output('download_window', 'is_open'),
        Output('download_file_xlsx', 'data'),
        Output('download_file_pdf', 'data')
    ],
    [
        Input('excel_download', 'n_clicks'),
        Input('pdf_download', 'n_clicks'),
        Input('download_window', 'n_clicks')
    ],
    [
        State('results_optimization', 'children'),
        State('address_session', 'data'), #test data
        State('optimized_results', 'children'),
        State('cluster_name_1', 'data')
    ]
)
def download_file(excelbtn, pdfbtn, closebtn, results_box, results_data, optimized_addresses, cluster):
    ctx = dash.callback_context
    if ctx.triggered:
        if results_box:
            if results_data:

                eventid = ctx.triggered[0]['prop_id'].split('.')[0]

                if excelbtn and eventid == 'excel_download':
                
                    ordered_addresses = list()

                    for item in optimized_addresses[1]['props']['children']:
                        address = item['props']['children'][0]['props']['children']
                        ordered_addresses.append(address)

                    index_addresses = dict(zip(list(range(len(ordered_addresses))), ordered_addresses))
                    df_order = {"Address": index_addresses}
                    df_order = pd.DataFrame.from_dict(df_order)

                    # Download as Excel File
                    results_data = results_data[0]
                    results_data = pd.DataFrame.from_dict(results_data)
                    results_data['Address'] = results_data['Address'].apply(lambda x : x if cluster in x else x + ', {}'.format(cluster))

                    # Be sure to check for the integrity of the submitted data. App might forget Recipient/Cell Number/misc info when merged
                    # with the reference table (df_order)
                    new_df = df_order.merge(results_data, on='Address', how='left', copy=False)

                    download_fxn = dcc.send_data_frame(new_df.to_excel, 'optimized_address_data.xlsx', sheet_name='final', index=False)

                    no_update = dash.no_update
                    alert_text = ''
                    alert_color = ''
                    alert_open = False
                    window_open = True

                    return [alert_color, alert_text, alert_open, window_open, download_fxn, no_update]
                
                elif pdfbtn and eventid == 'pdf_download': # PDF download currently not working as intended. Excel only functioning downloadable

                    ordered_addresses = list()

                    for item in optimized_addresses[1]['props']['children']:
                        address = item['props']['children'][0]['props']['children']
                        ordered_addresses.append(address)

                    index_addresses = dict(zip(list(range(len(ordered_addresses))), ordered_addresses))
                    df_order = {"Address": index_addresses}
                    df_order = pd.DataFrame.from_dict(df_order)

                    # Download as PDF File
                    results_data = results_data[0]
                    results_data = pd.DataFrame.from_dict(results_data)
                    results_data['Address'] = results_data['Address'].apply(lambda x : x if cluster in x else x + ', {}'.format(cluster))

                    # Be sure to check for the integrity of the submitted data. App might forget Recipient/Cell Number/misc info when merged
                    # with the reference table (df_order)
                    new_df = df_order.merge(results_data, on='Address', how='left', copy=False)

                    def write_pdf(bytes_io):
                        pdf = save_pdf.save_pdf(new_df) #√
                        bytes_io.write(pdf.encode('latin-1'))

                    no_update = dash.no_update
                    alert_text = ''
                    alert_color = ''
                    alert_open = False
                    window_open = True

                    return [alert_color, alert_text, alert_open, window_open, no_update, send_bytes(write_pdf, "optimized_route.pdf")]

                elif closebtn and eventid == 'download_window':

                    # close download modal window
                    alert_text = ''
                    alert_color = ''
                    alert_open = False
                    window_open = False

                    return [alert_color, alert_text, alert_open, window_open] # 2 missing output params
                
                else:
                    raise PreventUpdate
            else:
                no_update = dash.no_update
                alert_text = "Check the integrity of your data before proceeding."
                alert_color = 'warning'
                alert_open = True

                return [alert_color, alert_text, alert_open, no_update] # 2 missing output params
        else:
            no_update = dash.no_update
            alert_text = "Please process the addresses before proceeding!"
            alert_color = 'warning'
            alert_open = True

            return [alert_color, alert_text, alert_open, no_update] # 2 missing output params

    else:
        raise PreventUpdate