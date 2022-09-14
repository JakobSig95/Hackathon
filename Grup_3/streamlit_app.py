
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib.patches import ConnectionPatch
import plotly.express as px

st.title('Shark Attacks')

data = pd.read_csv('https://raw.githubusercontent.com/Alphambarushimana/Grup_3/main/attacks.csv', encoding='iso8859-1')

fig = px.pie(sex_attacks, values=sex_attacks.values, names=sex_attacks.index, title='Shark Attacks by Gender')
fig.update_layout(height=500, width=600)
fig.show()
