import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

@st.cache
def get_countries_data(): 
    url = "https://github.com/alanjones2/CO2/raw/master/data/countries_df.csv"
    return pd.read_csv(url)
@st.cache
def get_continent_data():
    url = 'https://github.com/alanjones2/CO2/raw/master/data/continents_df.csv'
    return pd.read_csv(url)
@st.cache
def get_world_data():
    url = 'https://github.com/alanjones2/CO2/raw/master/data/world_df.csv'
    return pd.read_csv(url)
@st.cache
def get_group_data():
    url = 'https://github.com/alanjones2/CO2/raw/master/data/income_types_df.csv'
    return pd.read_csv(url)

#st.set_page_config(layout = "wide")

df_countries= get_countries_data()
df_continents= get_continent_data()
df_world = get_world_data()
df_groups = get_group_data()

continents = df_continents['Entity'].unique()

df_countries
df_continents
df_world
df_groups

# Slider example - 

year = st.slider('Select year',1850,2020)

max = df_countries['Annual CO₂ emissions'].max()

fig1 = px.choropleth(df_countries[df_countries['Year']==year], locations="Code",
                    color="Annual CO₂ emissions",
                    hover_name="Entity",
                    range_color=(0,max),
                    color_continuous_scale=px.colors.sequential.Blues)
st.plotly_chart(fig1)


# Select slider example

start_month, end_month = st.select_slider(
    'Select a range of months',
    options=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    value=('Jan', 'Dec'))

st.write('You selected months between', start_month, 'and', end_month)

# Selectbox example

selected_continent = st.selectbox('Select country or group',continents)

df = df_continents[df_continents['Entity'] == selected_continent]
fig2 = px.line(df,"Year","Annual CO₂ emissions")
st.plotly_chart(fig2)

# Multiselect example

selected_continents = st.multiselect('Select country or group',continents,continents)

df = df_continents[df_continents['Year'] >= 2010]
df = df[df_continents['Entity'].isin(selected_continents)]

fig3 = px.bar(df,"Year","Annual CO₂ emissions",color="Entity", barmode='group')
st.plotly_chart(fig3)

# Radio button example

chart = st.radio(
    "Select the chart that you would like to display",
    ('World Map', 'Continent Emissions', 'Comparing continents'))

if chart == 'World Map': 
    st.plotly_chart(fig1)
if chart == 'Continent Emissions': 
    st.plotly_chart(fig2)
if chart == 'Comparing continents': 
    st.plotly_chart(fig3)

