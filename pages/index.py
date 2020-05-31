# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            #### Montgomery County Crime Prediction

            Born out of a curiosity to know how my intuition matched with the data in regards to crime levels in my childhood city and state.
            Montgomery Crime Predictor is trained on a RandomForest Model with ~40k observations. Using features such as
            Crime Type, location, and Place, this model attempts to predict the Street Location where crime will occur.
            This was a project made for learning and as a Unit Assesment for Unit 2 at [lambda School](https://lambdaschool.com/). \n

            Try it out by clicking on the button below!

            """
        ),
        dcc.Link(dbc.Button('Predict The Crime',
                            color='primary'), href='/predictions')
    ],
    md=4,
)


# Logic for plotting a graph in the home page
df = pd.read_csv('notebooks/Cleaned_Crime.csv')
available_indicators = df['Street Name'].unique()

# Terrain Plot... pretty cool
fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
                        color='Street Name', opacity=0.1)
fig.update_layout(mapbox_style='stamen-terrain')
fig.show()

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
