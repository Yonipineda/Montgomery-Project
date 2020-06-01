# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.H2("Process: Messy data, Data Wrangling -> Model Training."),
        dcc.Markdown(
            """

            Trying to find a solution yet alone a problem to address with any dataset
            is challenging in of itself. In some cases, it requires some domain knowledge
            of the data you are inspecting. Data is also very messy, chaos insues in data.
            There can be order, and a pattern can be found which can lead to insightful findings.
            Lets take a look at how the data came in as I started:

            ![messy](/assets/messy.gif) 

            There were a number of missing values, parsing the data was a challenge and, when it came
            to structuring it for training, much more needed to be done.





            """
        ),

    ],
)

layout = dbc.Row([column1])
