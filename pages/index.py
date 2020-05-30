# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

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
            Montgomery Crime Predictor is trained on a RandomForest Model with ~200,000 observations. Using features such as
            Time, location, and Place, this model attempts to predict the type of crime that will occur. This was a project
            made for learning and as a Unit Assesment for Unit 2 at [lambda School](https://lambdaschool.com/). \n

            Try it out by clicking on the button below!

            """
        ),
        dcc.Link(dbc.Button('Predict The Crime',
                            color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
