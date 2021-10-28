# -*- coding: utf-8 -*-
"""Lung Cancer sandbox.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lVte-2LyQd28jIrnA3mDlDFOolqjJEWf
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import plotly.express as px

f_name = '/content/drive/MyDrive/Programming for Data Science/Semester Project/Data/lung_cancer.csv'

lungCancer = pd.read_csv(f_name)

lungCancer_state = lungCancer._STATE.drop_duplicates()
lungCancer_state = list(lungCancer_state)

cdc_state = {1: 'Alabama', 
             2: 'Alaska', 
             4: 'Arizona',
             5: 'Arkansas',
             6: 'California',
             8: 'Colorado',
             9: 'Connecticut',
             10: 'Delaware',
             11: 'District of Columbia',
             12: 'Florida',
             13: 'Georgia',
             15: 'Hawaii',
             16: 'Idaho',
             17: 'Illinois',
             18: 'Indiana',
             19: 'Iowa',
             20: 'Kansas',
             21: 'Kentucky',
             22: 'Louisiana',
             23: 'Maine',
             24: 'Maryland',
             25: 'Massachusetts',
             26: 'Michigan',
             27: 'Minnesota',
             28: 'Mississippi',
             29: 'Missouri',
             30: 'Montana',
             31: 'Nebraska',
             32: 'Nevada',
             33: 'New Hampshire',
             34: 'New Jersey',
             35: 'New Mexico',
             36: 'New York',
             37: 'North Carolina',
             38: 'North Dakota',
             39: 'Ohio',
             40: 'Oklahoma',
             41: 'Oregon',
             42: 'Pennsylvania',
             44: 'Rhode Island',
             45: 'South Carolina',
             46: 'South Dakota',
             47: 'Tennessee',
             48: 'Texas',
             49: 'Utah',
             50: 'Vermont',
             51: 'Virginia',
             53: 'Washington',
             54: 'West Virginia',
             55: 'Wisconsin',
             56: 'Wyoming',
             66: 'Guam',
             72: 'Puerto Rico'}

cdc_abb = {
    'Alabama': 'AL', 
    'Alaska': 'AK', 
    'Arizona': 'AZ', 
    'Arkansas': 'AR', 
    'California': 'CA', 
    'Colorado': 'CO', 
    'Connecticut': 'CT', 
    'Delaware': 'DE', 
    'District of Columbia': 'DC', 
    'Florida': 'FL', 
    'Georgia': 'GA', 
    'Hawaii': 'HI', 
    'Idaho': 'ID', 
    'Illinois': 'IL', 
    'Indiana': 'IN', 
    'Iowa': 'IA', 
    'Kansas': 'KS', 
    'Kentucky': 'KY', 
    'Louisiana': 'LA', 
    'Maine': 'ME', 
    'Maryland': 'MD', 
    'Massachusetts': 'MA', 
    'Michigan': 'MI', 
    'Minnesota': 'MN', 
    'Mississippi': 'MS', 
    'Missouri': 'MO', 
    'Montana': 'MT', 
    'Nebraska': 'NE', 
    'Nevada': 'NV', 
    'New Hampshire': 'NH', 
    'New Jersey': 'NJ', 
    'New Mexico': 'NM', 
    'New York': 'NY', 
    'North Carolina': 'NC', 
    'North Dakota': 'ND', 
    'Ohio': 'OH', 
    'Oklahoma': 'OK', 
    'Oregon': 'OR', 
    'Pennsylvania': 'PA', 
    'Rhode Island': 'RI', 
    'South Carolina': 'SC', 
    'South Dakota': 'SD', 
    'Tennessee': 'TN', 
    'Texas': 'TX', 
    'Utah': 'UT', 
    'Vermont': 'VT', 
    'Virginia': 'VA', 
    'Washington': 'WA', 
    'West Virginia': 'WV', 
    'Wisconsin': 'WI', 
    'Wyoming': 'WY', 
    'Guam': 'GU', 
    'Puerto Rico': 'PR'
}

# Name of states with response to lung cancer
print(len([cdc_state[x] for x in lungCancer_state]), '\n', [cdc_state[x] for x in lungCancer_state])

LCS_state_counts = lungCancer['_STATE'].value_counts().rename_axis('abb').reset_index(name='counts')

test = lungCancer['_STATE'].value_counts().to_frame(name = 'count').reset_index()

LCS_state_counts

LCS_state_counts.iloc[:,0]

LCS_state_counts

state_df = pd.read_csv('/content/drive/MyDrive/Programming for Data Science/Semester Project/Scripts/state_df.csv')

fig = px.choropleth(state_df,  # Input Pandas DataFrame
                    locations="state",  # DataFrame column with locations
                    color="value",  # DataFrame column with color values
                    hover_name="state", # DataFrame column hover info
                    locationmode = 'USA-states') # Set to plot as US States

fig.show()

lungCancer[lungCancer['INCOME2'].isnull()]

lungCancer[lungCancer['_SEX'].isnull()]

lungCancer[lungCancer['MARITAL'].isnull()]

lungCancer[lungCancer['EMPLOY1'].isnull()]

lungCancer[lungCancer['_INCOMG'].isnull()]

lungCancer[lungCancer['WEIGHT2'].isnull()]

lungCancer[lungCancer['HEIGHT3'].isnull()]

import seaborn as sns

lungCancer.dropna(inplace=True)
sns.heatmap(data=lungCancer.isna(), cmap='plasma', cbar=False)