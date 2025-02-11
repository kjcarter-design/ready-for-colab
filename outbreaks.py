import requests
import pandas as pd
import numpy as np
import plotly.express as px

url = 'https://raw.githubusercontent.com/jimcody2014/python_data/refs/heads/main/Immunotherapy.csv'

pdf = pd.read_csv('https://raw.githubusercontent.com/jimcody2014/python_data/refs/heads/main/outbreaks2.csv',header = None,
names = ('year','month','state','location','food','species','status','illness','hospitalizations','fatalities'),usecols = [0,1,2,3,4,5,7,9,10,11])
pdf.shape
pdf.head()
print (pdf)