# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from joblib import load, dump
import shap

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# read in the data
df = pd.read_csv('notebooks/Cleaned_Crime.csv')
print(f"CSV LOADED: {df}")

# load in the RandomForest classifier model
pipeline = load('notebooks/big_finalized_model.joblib')
print(f"MODEL LOADED: {pipeline}")

# Features/options
available_zip = sorted(df['Zip Code'].unique())
available_sector = sorted(df['Sector'].unique())
available_police = sorted(df['Police District Name'].unique())
available_city = sorted(df['City'].unique())
available_place = sorted(df['Place'].unique())
available_year = sorted(df['Year'].unique())
available_month = sorted(df['Month'].unique())
available_hour = sorted(df['Hour'].unique())
available_min = sorted(df['Minute'].unique())

style = {'padding': '1.5em'}

column1 = dbc.Col([
    dcc.Markdown(
        """
            # **Make A Prediction**

            Select among the given choices and recieve a prediction of the name of the street
            where a crime may occur.\n

            Note: Month is set as a Numerical representation and Hour is in Military Time.
            """
    ),
    html.Div([
        dcc.Markdown("##### Zip Code"),
        dcc.Dropdown(
            id='zip_dd',
            options=[
                {'label': i, 'value': i} for i in available_zip],
            value='20902'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Sector"),
        dcc.Dropdown(
            id='sector_dd',
            options=[
                {'label': i, 'value': i} for i in available_sector],
            value='L'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Police District"),
        dcc.Dropdown(
            id='sector_dd',
            options=[
                {'label': i, 'value': i} for i in available_police],
            value='WHEATON'
        )
    ]),
    html.Div([
        dcc.Markdown("##### City"),
        dcc.Dropdown(
            id='city_dd',
            options=[
                {'label': i, 'value': i} for i in available_city],
            value='SILVER SPRING'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Place"),
        dcc.Dropdown(
            id='place_dd',
            options=[
                {'label': i, 'value': i} for i in available_place],
            value='Parking Lot - Commercial'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Year"),
        dcc.Dropdown(
            id='year_dd',
            options=[
                {'label': i, 'value': i} for i in available_year],
            value='2020'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Month"),
        dcc.Dropdown(
            id='month_dd',
            options=[
                {'label': i, 'value': i} for i in available_month],
            value='2'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Hour"),
        dcc.Dropdown(
            id='hour_dd',
            options=[{'label': i, 'value': i} for i in available_hour],
            value='5'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Minute"),
        dcc.Dropdown(
            id='minute_dd',
            options=[{'label': i, 'value': i} for i in available_min],
            value='20'
        )
    ]),

],
    md=3

)

column2 = dbc.Col([
    dcc.Markdown('### Predicted Street where crime will occur',
                 className='mb-4'),
    dcc.Markdown('#### Based on Time, Place, and Location',
                 className='mb-4'),
    dcc.Markdown('#### Trained on ~40k observations', className='mb-4'),
    html.Div(id='prediction-content',
             style={'textAlign': 'center', 'fontsize': 72

                    }

             ),
    html.Div(
        id='euphemism',
        style={
            'textAlign': 'center',
            'fontSize': '30',
        }
    )

],
    md=6
)


@app.callback(
    [Output('prediction-content', 'children')],
    [Input('zip_dd', 'value'),
     Input('sector_dd', 'value'),
     Input('police_dd', 'value'),
     Input('city_dd', 'value'),
     Input('place_dd', 'value'),
     Input('year_dd', 'value'),
     Input('month_dd', 'value'),
     Input('hour_dd', 'value'),
     Input('minute_dd', 'value')])
def predict_and_plot(place_dd, city_dd, sector_dd, police_dd, zip_dd, year_dd,
                     month_dd, hour_dd, minute_dd):

    pred_df = pd.DataFrame(
        columns=['Zip Code', 'Sector', 'Police District Name', 'City',
                 'Place', 'Year', 'Month', 'Hour', 'Minute'],
        data=[[zip_dd, sector_dd, police_dd, city_dd, place_dd,
               year_dd, month_dd, hour_dd, minute_dd]]
    )

    print(f"DF FOR PREDICTION SET: {pred_df}")

    y_pred = pipeline.predict(pred_df)[0]

    y_pred_pos = np.clip(y_pred, a_min=0, a_max=20)

    pred_out = y_pred_pos

    return pred_out


column3 = dbc.Col([


])


layout = dbc.Row([column1, column2])
