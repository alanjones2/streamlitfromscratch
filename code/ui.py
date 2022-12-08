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

df_countries
df_continents
df_world
df_groups

def map():
    max = df_countries['Annual CO₂ emissions'].max()

    year = st.slider('Select year',1850,2020)
    fig = px.choropleth(df_countries[df_countries['Year']==year], locations="Code",
                        color="Annual CO₂ emissions",
                        hover_name="Entity",
                        range_color=(0,max),
                        color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig, use_container_width=True)

map()

def continents_bar_graph():

    continents = df_continents['Entity'].unique()

    selected_continents = st.multiselect('Select country or group',continents,continents)#,default_continents)

    df = df_continents[df_continents['Year'] >= 2010]

    df = df[df_continents['Entity'].isin(selected_continents)]

    fig = px.bar(df,"Year","Annual CO₂ emissions",color="Entity", barmode='group')

    st.plotly_chart(fig, use_container_width=True)

continents_bar_graph()

start_month, end_month = st.select_slider(
    'Select a range of months',
    options=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    value=('Jan', 'Dec'))
    
st.write('You selected months between', start_month, 'and', end_month)