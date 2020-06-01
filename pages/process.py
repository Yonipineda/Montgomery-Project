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
        html.H2("Process: Messy data -> Data Wrangling -> Model Training"),
        dcc.Markdown(
            """
            #### Messy Data \n

            Trying to find a solution yet alone a problem to address with any dataset
            is challenging in of itself. In some cases, it requires some domain knowledge
            of the data you are inspecting. Data is also very messy, chaos insues in data.
            There can be order, and a pattern can be found which can lead to insightful findings.
            Lets take a look at how the data came in as I started:

            ![messy](/assets/messy.gif)

            The original file contained over 200k observations. There were a number of missing values,
            parsing the data was a challenge and, when it came to structuring it for training,
            much more needed to be done. The next step was wrangling the data and preparing it
            for model ingection and even some cool visualizations.\n

            #### Wrangling and Grunt Work \n

            Much of the grunt work had to do with To Datetime conversion, data type conversion,
            byte encoding, removing unique observations in some columns, such as city/street name,
            that did not meet a certain threshold, filling in NaN's and dropping what remained, and
            removing columns that could cause leakage or over-fitting. This gif animation
            shows a couple of functions that displays that work:

            ![wrangling](/assets/wrangling.gif) \n

            #### Cleaned Data Ready For Action \n

            Now, with the cleaned data:

            ![cleaned](/assets/cleaned.gif)

            I went ahead and began some pre-processing for training. \n

            #### Pre-Processing and Model Tuning. \n

            I did two splits, a 80/20 for the Train and Test split, and another
            80/20 for the Train and validation split. I ended with a shape of: \n

            Split Shape: Train (24348, 27), Validate (6088, 27), Test (7610, 27) \n

            And, selected my target, that being 'Street Name' and the features to train.

            ![cleaned](/assets/preprocess.gif) \n


            #### Final Model 










            """
        ),

    ],
)

layout = dbc.Row([column1])
