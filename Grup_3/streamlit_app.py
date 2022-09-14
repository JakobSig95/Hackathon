
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib.patches import ConnectionPatch
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/Alphambarushimana/Grup_3/main/attacks.csv', encoding='iso8859-1')

data #showing the data




data.isna().sum()

data.drop(['Case Number', 'Name', 'Injury', 'Time', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis = 1, inplace = True)






# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Sex ':'Gender'})

data.Gender.unique()

# sort the unique values in column Gender into three categories: Female, Male and Unknown

data['Gender'] =  data['Gender'].replace(['M','M ', 'N'],'Male')
data['Gender'] =  data['Gender'].replace(['F'],'Female')
data['Gender'] =  data['Gender'].replace(['.','lli'],'Unknown')
data['Gender'] = data['Gender'].fillna('Unknown')

data.Gender.value_counts()

#from 1900 to 2018
sex_attacks = data.groupby('Gender')['Gender'].count()
sex_attacks = sex_attacks[(sex_attacks.index == 'Male') | (sex_attacks.index=='Female')|(sex_attacks.index=='Unknown')]
sex_attacks

fig = px.pie(sex_attacks, values=sex_attacks.values, names=sex_attacks.index, title='Shark Attacks by Gender')
fig.update_layout(height=500, width=600)
fig.show()

#from 2010 - 2018 
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

# Test plot

byYear_attack = data.groupby('Year')['Date'].count().reset_index()
fig = px.line(byYear_attack,x='Year', y='Date', title='Shark Attack by Year')
fig.show()



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



# Fatality

# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Fatal (Y/N)':'Fatality'})

data.Fatality.unique()

# sort the unique values in column Fatality into three categories: No, Yes and Unknown

data['Fatality'] =  data['Fatality'].replace(['N', ' N', 'N '],'No')
data['Fatality'] =  data['Fatality'].replace(['Y'],'Yes')
data['Fatality'] =  data['Fatality'].replace(['UNKNOWN', 'M', '2017'],'Unknown')
data['Fatality'] = data['Fatality'].fillna('Unknown')

data.Fatality.value_counts()

data.info()

Mydata = data.groupby(['Fatality', 'Gender'], as_index=False).size()
Mydata = Mydata.sort_values(by=['size'], ascending=False)
Mydata = Mydata[0:7]
Mydata.drop([5],inplace=True)

Mydata.drop([4],inplace=True)
Mydata.drop([6],inplace=True)
Mydata.head()

import plotly.express as px
mlabels=['Male Non Fatal', 'Male fatael','Female Non Fatal','Female Fatal']
fig = px.pie(Mydata, names=mlabels,values='size',hole = 0.8)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.update_layout(
    annotations=[dict(text="comparison of accidents", x=0.5, y=0.5, font_size=20, showarrow=False)])
fig.update_layout(showlegend=False)

# Location

len(data.Country.unique())

# Top five countries with most shark attacks

data['Country'].value_counts().head(5)

# Top five countries with least shark attacks

data['Country'].value_counts().tail(5)

# Attacks by country

attacks_by_country = data['Country'].value_counts().reset_index().rename(columns={'Country':'Count','index':'Country'})
attacks_by_country.head()

# World map of attacks by country
world_map = px.choropleth(attacks_by_country,
                    locations = 'Country',
                    color = 'Count',
                    color_continuous_scale='Plasma',
                    locationmode = 'country names',
                    scope = 'world',
                    title = 'Shark attacks around the World',
                    labels = {'Count':'Shark attacks'}
                    )

world_map.update_geos(fitbounds="locations", visible=False)
world_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

world_map.show()


st.title('Shark Attacks')


tab1, tab2, tab3 = st.tabs(["Pie", "Map", "Line"])
fig = [tab1]

with tab1:
   st.header("A Pie")
   
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

