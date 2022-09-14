
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib.patches import ConnectionPatch
import plotly.express as px

st.title('Shark Attacks')

data = pd.read_csv('https://raw.githubusercontent.com/Alphambarushimana/Grup_3/main/attacks.csv', encoding='iso8859-1')

data

data.info()

data.isna().sum()

data.drop(['Case Number', 'Name', 'Injury', 'Time', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis = 1, inplace = True)

data.info()

data.columns

data = data.rename(columns = {'Sex ':'Gender'})

data.Gender.unique()

data['Gender'] =  data['Gender'].replace(['M','M ', 'N'],'Male')
data['Gender'] =  data['Gender'].replace(['F'],'Female')
data['Gender'] =  data['Gender'].replace(['.','lli'],'Unknown')
data['Gender'] = data['Gender'].fillna('Unknown')

data.Gender.value_counts()

sex_attacks = data.groupby('Gender')['Gender'].count()
sex_attacks = sex_attacks[(sex_attacks.index == 'Male') | (sex_attacks.index=='Female')|(sex_attacks.index=='Unknown')]
sex_attacks

fig = px.pie(sex_attacks, values=sex_attacks.values, names=sex_attacks.index, title='Shark Attacks by Gender')
fig.update_layout(height=500, width=600)
fig.show()

sex_attacks_2010_2018 = data[data.Year >= 2010].groupby('Gender')['Gender'].count()
sex_attacks_2010_2018 = sex_attacks_2010_2018[(sex_attacks_2010_2018.index == 'Male') | (sex_attacks_2010_2018.index =='Female')| (sex_attacks_2010_2018.index=='Unknown')]
sex_attacks

fig = px.pie(sex_attacks_2010_2018, values=sex_attacks_2010_2018.values, names=sex_attacks_2010_2018.index, 
             title='Shark Attacks by Gender - Between 2010-2018')
fig.update_layout(height=500, width=600)
fig.show()

data.Year.unique()

data = data[data['Year'] >= 1900]

data.Year.unique()

byYear_attack = data.groupby('Year')['Date'].count().reset_index()
fig = px.line(byYear_attack,x='Year', y='Date', title='Shark Attack by Year')
fig.show()
