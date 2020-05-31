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
available_crime = sorted(df['Crime_Type'].unique())
available_month = sorted(df['Month'].unique())
available_hour = sorted(df['Hour'].unique())
available_min = sorted(df['Minute'].unique())
available_victim = sorted(df['Victims'].unique())

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
        dcc.Markdown("###### Crime Type "),
        dcc.Dropdown(
            id='crime-dd',
            options=[
                {'label': i, 'value': i} for i in available_crime],
            value='Crime Against Society'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Victims"),
        dcc.Dropdown(
            id='victims-dd',
            options=[
                {'label': i, 'value': i} for i in available_victim],
            value='2'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Month"),
        dcc.Dropdown(
            id='month-dd',
            options=[
                {'label': i, 'value': i} for i in available_month],
            value='1'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Hour "),
        dcc.Dropdown(
            id='hour-dd',
            options=[
                {'label': i, 'value': i} for i in available_hour],
            value='5'
        )
    ]),
    html.Div([
        dcc.Markdown("###### Minute"),
        dcc.Dropdown(
            id='minute-dd',
            options=[
                {'label': i, 'value': i} for i in available_min],
            value='20'
        )
    ]),

],
    md=3

)

column3 = dbc.Col([
    dcc.Markdown("##### Set Approximate Year"),
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
     Input('crime-dd', 'value'),
     Input('victims-dd', 'value'),
     Input('month-dd', 'value'),
     Input('hour-dd', 'value'),
     Input('minute-dd', 'value')])
def predict_and_plot(
        place, crime, victims, month, hour,
        minute):
    # Create prediction
    pred_df = pd.DataFrame(
        columns=['Place', 'Crime_Type', 'Victims', 'Month', 'Hour',
                 'Minute'],
        data=[[place, crime, victims, month, hour, minute]]
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

    condensed_names = ['Place', 'Crime', 'Victims', 'Month',
                       'Hour', 'Minute']

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
