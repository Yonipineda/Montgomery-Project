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

# Features/options
available_place = sorted(df['Place'].unique())
available_city = sorted(df['City'].unique())
available_sector = sorted(df['Sector'].unique())
available_police = sorted(df['Police District Name'].unique())
available_zip = sorted(df['Zip Code'].unique())
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
        dcc.Markdown("###### Place"),
        dcc.Dropdown(
            id='place-dd',
            options=[
                {'label': i, 'value': i} for i in available_place],
            value='Street - In vehicle'
        )
    ]),
    html.Div([
        dcc.Markdown("###### City"),
        dcc.Dropdown(
            id='city-dd',
            options=[
                {'label': i, 'value': i} for i in available_city],
            value='SILVER SPRING'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Sector"),
        dcc.Dropdown(
            id='sector-dd',
            options=[
                {'label': i, 'value': i} for i in available_sector],
            value='L'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Police District"),
        dcc.Dropdown(
            id='police-dd',
            options=[
                {'label': i, 'value': i} for i in available_police],
            value='WHEATON'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Zip Code "),
        dcc.Dropdown(
            id='zip-dd',
            options=[
                {'label': i, 'value': i} for i in available_zip],
            value='20902.0'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Year"),
        dcc.Dropdown(
            id='year-dd',
            options=[
                {'label': i, 'value': i} for i in available_year],
            value='2020'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Month"),
        dcc.Dropdown(
            id='month-dd',
            options=[
                {'label': i, 'value': i} for i in available_month],
            value='2'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Hour"),
        dcc.Dropdown(
            id='hour-dd',
            options=[{'label': i, 'value': i} for i in available_hour],
            value='5'
        )
    ]),
    html.Div([
        dcc.Markdown("##### Minute"),
        dcc.Dropdown(
            id='minute-dd',
            options=[{'label': i, 'value': i} for i in available_min],
            value='20'
        )
    ]),

],
    md=3

)

column3 = dbc.Col([
    dcc.Markdown("#####  Select A Year"),
    dcc.Slider(
        id='year-slide',
        min=2019,
        max=2020,
        step=2,
        value=2020,
        marks={n: f'{n:.0f}' for n in range(2019, 2020, 2)}
    ),
    html.H4(id='prediction-content', style={'fontWeight': 'bold'}),
    html.Div(
        dcc.Graph(id='shap-plot')
    )

],
    md=6
)


@app.callback(
    [Output('prediction-content', 'children'),
     Output('shap-plot', 'figure')],
    [Input('place-dd', 'value'),
     Input('city-dd', 'value'),
     Input('sector-dd', 'value'),
     Input('police-dd', 'value'),
     Input('zip-dd', 'value'),
     Input('year-dd', 'value'),
     Input('month-dd', 'value'),
     Input('hour-dd', 'value'),
     Input('minute-dd', 'value')])
def predict_and_plot(
        place, city, sector, policedistrictname, zipcode,
        year, month, hour, minute):
    # Create prediction
    pred_df = pd.DataFrame(
        columns=['Place', 'City', 'Sector', 'Police District Name', 'Zip Code',
                 'Year', 'Month', 'Hour', 'Minute'],
        data=[[place, city, sector, policedistrictname, zipcode,
               year, month, hour, minute]]
    )

    pipe = load('notebooks/finalized_model.joblib')
    y_pred_log = pipe.predict(pred_df)
    y_pred = np.expm1(y_pred_log)[0]

    pred_out = f"Current Value: ${y_pred:,.2f}"

    # Derive shap values from user input
    encoder = pipe.named_steps['ordinalencoder']
    model = pipe.named_steps['randomforestclassifier']
    pred_df_encoded = encoder.transform(pred_df)
    explainer = load('notebooks/explainer.joblib')
    shap_vals = explainer.shap_values(pred_df_encoded)
    input_names = [i for i in pred_df.iloc[0]]

    # Create dataframe for shap plot
    shap_df = pd.DataFrame({'feature': pred_df.columns.to_list(),
                            'shap-val': shap_vals[0],
                            'val-name': input_names})
    # Create list of two different colors depending on shap-val
    colors = [
        '#0063D1' if value >= 0.0 else '#E43137' for value in shap_df['shap-val']
    ]

    condensed_names = ['Place', 'City', 'Sector', 'Police District Name',
                       'Zip Code', 'Year', 'Month', 'Hour', "Minute"]

    shap_plot = {
        'data': [
            {'x': shap_df['shap-val'], 'y': condensed_names,
             'type': 'bar', 'orientation':'h', 'hovertext': shap_df['val-name'],
             'marker': {'color': colors}, 'opacity': 0.8}],
        'layout': {
            'title': 'Atrribute Impact on Prediction',
            'transition': {'duration': 250}}
    }

    return pred_out, shap_plot


column2 = dbc.Col([


])


layout = dbc.Row([column1, column3])
