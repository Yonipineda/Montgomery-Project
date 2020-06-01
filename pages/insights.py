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
        html.H2("Insights"),

        dcc.Markdown(

            """

            I went into this project with biased predictions due to years of experience
            in these parts. I knew some parts were known to be a bit more risky, whether
            it was true or not, possibly just talk. I had already built images of these
            different places in Montgomery County. It is generally known that at night
            time, risk increases: this was true in this case. It seems Time -- the hour
            of the day, month of the year, and even minute of the hour can predict if
            a crime will occur in a given street. Location was another one, it seems
            certain Zip Code were I predictor. Now, I do want to stress that this in no
            way should be taken seriously, this is the work of a student with no more than
            a couple of months with programming experience and just enough understanding
            of statistics to be able to do just to data. Below is a picture illustrating
            the Feature Importance for Street Name Prediction:

            """
        ),
        html.Img(src='assets/feature_importance.png', className='img-fluid'),
        html.Br(),
        html.Div([

            html.Br(),
            html.P(
                """
                    This next illustration, is a eli5 Permutation Feature Importance Graph.
                    Shows sector and Zip Code holding the majority of the weight.

                    """
            ),
            html.Img(src='assets/permutation.png', className='img-fluid')

        ]),
        html.Br(),
        html.Div([

            dcc.Markdown(
                '''
            In this gif animation below, you can see a [Partial Dependece Plot](https://blogs.sas.com/content/subconsciousmusings/2018/06/12/interpret-model-predictions-with-partial-dependence-and-individual-conditional-expectation-plots/).
            The line represents change in prediction based on adjustment of the features value. It is a PDP
            of Zip Code and Hour in relation to Street Name.

            ![header](/assets/PDP.gif)

            '''
            ),
        ])

    ],
    md=10
)

layout = dbc.Row([column1])
