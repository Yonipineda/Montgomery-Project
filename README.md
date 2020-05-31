# Montgomery County, MD Crime Predictor Project

---

## Dash app

In development. Going over unfinished work and will be deployed sometime soon.

---

## Installation

##### clone the master branch to your local machine
```
>> git clone https://github.com/Yonipineda/Montgomery-Project.git
```

##### Create virtual environment and install requirements.txt
```
>> pipenv install requirements.txt
```
NOTE: *OPTIONAL*


##### If you did the previous step and created an environment for this project, open the env
```
>> pipenv shell
```

---

## Run the Dash app locally and start building!

##### run it by executing the following line
```
>> python run.py
```

##### Now, follow along [Ryan Herr's](https://lambdaschool.github.io/ds/unit2/dash-template/) guide and build as you will.

---

## Data

- The data source can be found at [dataMontgomery](https://data.montgomerycountymd.gov/Public-Safety/Crime/icn6-v9z3)

- The cleaned data can be found in the notebooks folder, named [Cleaned_Crime.csv](notebooks/Cleaned_Crime.csv)

- The smaller size cleaned data can be found in the notebooks folder, named [sml_crime.csv](sml_crime.csv)

---

## Notebooks

All of the data exploration can be found there.

- For the cleaning process, refer to [Montgomery_Cleaning.ipynb](notebooks/Montgomery_Cleaning.ipynb)

- For the visual creation process, refer to [Montgomery_Visualization.ipynb](notebooks/Montgomery_Visualization.ipynb)

- For the Model Process, refer to [Montgomery_Model.ipynb](notebooks/Montgomery_Model.ipynb)

The basis for this project has to do with wanting to find out how my intuition matched with the data on crime occurance in Montgomery County, MD; being where I lived for the majority of my childhood.

This project was our Unit2 Final Project at [Lambda](https://lambdaschool.com/).

---

## Model

- The joblib file can be found here [finalized_model.joblib](notebooks/finalized_model.joblib)

- The explainer shap model can be found here [explainer.joblib](notebooks/explainer.joblib)

---

## Medium Article

Find the short read [here](https://medium.com/@yonipineda1010/predicting-type-of-crime-in-montgomery-county-md-26a4b375948)
