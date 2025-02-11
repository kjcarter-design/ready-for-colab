import requests
import pandas as pd
import numpy as np
import plotly.express as px

response = requests.get("https://data.cdc.gov/resource/saz5-9hgg.json")
jsonhold = response.json()

# Put the data into a DataFrame

vaccines = pd.DataFrame(jsonhold)

# Create month and week columns

vaccines['month'] = pd.to_datetime(vaccines['week_of_allocations']).dt.month
vaccines['day'] =  pd.to_datetime(vaccines['week_of_allocations']).dt.day


# Changing the datatypes & column names

vaccines['month'] = vaccines.month.astype(str)
vaccines['day'] = vaccines.day.astype(str)
vaccines['_1st_dose_allocations'] = pd.to_numeric(vaccines['_1st_dose_allocations']).astype(int)
vaccines['_2nd_dose_allocations'] = pd.to_numeric(vaccines['_2nd_dose_allocations']).astype(int)
vaccines['_2nd_dose_allocations'] = vaccines._2nd_dose_allocations*1.2


short_names = {'_1st_dose_allocations':'first',
               '_2nd_dose_allocations':'second'}
vaccines.rename(columns=short_names, inplace=True)
vaccines = vaccines[vaccines.jurisdiction.isin(['Massachusetts','New Hampshire', 'Rhode Island'])]


vaccines.head()