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


st.set_page_config(layout = "wide")

df_countries= get_countries_data()
df_continents= get_continent_data()
df_world = get_world_data()
df_groups = get_group_data()

df_countries
df_continents
df_world
df_groups

st.markdown("""
# World CO2 emissions
__The graphs below show the CO2 emissions per capita for the entire 
world and individual countries over time.
Select a year with the slider in the left-hand graph and countries 
from the drop down menu in the other one.__

__Scroll down to see charts demonstrating the correlation between 
the level of CO2 and global warming.__

__Hover over any of the charts to see more detail__

---

""")

col2, space2, col3 = st.columns((10,1,10))

with col2:
    year = st.slider('Select year',1850,2020)
    fig = px.choropleth(df_countries[df_countries['Year']==year], locations="Code",
                        color="Annual CO₂ emissions",
                        hover_name="Entity",
                        range_color=(0,12000000000),
                        color_continuous_scale=px.colors.sequential.Reds)
    st.plotly_chart(fig, use_container_width=True)

with col3: 

    fig2 = px.line(df_world,"Year","Annual CO₂ emissions including land-use change")

    st.plotly_chart(fig2, use_container_width=True)


col4, space3, col5,space4,col6 = st.columns((10,1,10,1,10))
with col4:
    st.markdown("""
    ## Corelation between CO2 emission and global warming

    This can be seen in the adjacent graphs. 
    
    The first show temperature
    has changed since 1850 and you can see that temperatures begin 
    to rise after the beginning of the twentieth century but there 
    is a sharp upturn in that rise about mid-way through (the scatter
    points are the actual figures for each year and the line is a 
    lowess smoothing of those points so that we can more easily see 
    the trend).

    The second graph shows the rise in total CO2 emissions over the 
    same period and a similar trend can be seen with a sharp rise in 
    emissions mid-twentieth century.
    """)
with col5:
    default_continents = ['Africa','North America','Asia', 'Europe']
    continents = df_continents['Entity'].unique()

    selected_continents = st.multiselect('Select country or group',continents,default_countries)

    df5 = df_continents.query('Entity in @selected_countries' )

    fig2 = px.line(df3,"Year","Annual CO₂ emissions",color="Entity")

    st.plotly_chart(fig2, use_container_width=True)

with col6:
    default_countries = ['United States','United Kingdom','China', 'Australia']
    countries = df_countries['Entity'].unique()

    selected_countries = st.multiselect('Select country or group',countries,default_countries)

    df6 = df_countries.query('Entity in @selected_countries' )

    fig2 = px.line(df3,"Year","Annual CO₂ emissions",color="Entity")

    st.plotly_chart(fig2, use_container_width=True)








st.markdown('__Data Source:__ _Our World in Data CC BY_')