
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib.patches import ConnectionPatch
import plotly.express as px

st.title('Shark Attacks')

## Activities

data.Activity.unique()

len(data["Activity"].unique())

data.Activity.value_counts().head(10)

## TYPE
data.Type.unique()

# Here making only 1 type, ALlType, so not 9 different provoked unprovked ETC.

data.loc[(data['Type'] == 'Boating') | (data['Type'] == 'Boatomg') | (data['Type'] == 'Boat') | (data['Type'] == 'Questionable') | (data['Type'] == 'Sea Disaster') | (data['Type'] == 'Invalid') | (data['Type'] == 'Provoked') | (data['Type'] == 'Unprovoked'), "Type"] = "AllType"
byType_count = data['Type'].value_counts().reset_index().rename(columns={'Type':'Count','index':'Type'})
byType_count

# Total amount of attacks based on activity

prov_activity = data[data.Type == 'AllType'].groupby('Activity')['Activity'].count().sort_values(ascending=False)[:10]

fig = px.bar(prov_activity, x=prov_activity.values, y=prov_activity.index, orientation='h', labels={'index':'','x':'Attack Count'},
            title = 'Shark Attacks by Activity')
fig.update_layout(height=600, width=900)
fig.show()

# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Fatal (Y/N)':'Fatality'})

data.Fatality.unique()

# sort the unique values in column Fatality into three categories: No, Yes and Unknown

data['Fatality'] =  data['Fatality'].replace(['N', ' N', 'N '],'No')
data['Fatality'] =  data['Fatality'].replace(['Y'],'Yes')
data['Fatality'] =  data['Fatality'].replace(['UNKNOWN', 'M', '2017'],'Unknown')
data['Fatality'] = data['Fatality'].fillna('Unknown')

data.Fatality.value_counts()
