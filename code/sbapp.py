import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Get the data and cache it
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

# Assign the data to dataframes
df_countries= get_countries_data()
df_continents= get_continent_data()
df_world = get_world_data()
df_groups = get_group_data()

# A list of all of the continents
continents = df_continents['Entity'].unique()

# The side bar that contains radio buttons for selection of charts
with st.sidebar:
    st.header('Select an chart to be displayed')
    chart = st.radio(
    "Select the image that you would like to display",
    ('World Map', 'Continent Emissions', 'Comparing continents'))

# The main window

st.title("A Simple CO2 Emissions Dashboard")
st.write("an example of a Streamlit layout using a sidebar")

with st.container():
    
    if chart == 'World Map': 

        st.header("Global emissions since 1850")
        st.info("""Select a year with the slider to see the intensity
                of emissions change in each country""")

        year = st.slider('Select a year',1850,2020)

        max = df_countries['Annual CO₂ emissions'].max()

        fig1 = px.choropleth(df_countries[df_countries['Year']==year], locations="Code",
                            color="Annual CO₂ emissions",
                            hover_name="Entity",
                            range_color=(0,max),
                            color_continuous_scale=px.colors.sequential.Blues)
        st.plotly_chart(fig1)

    if chart == 'Continent Emissions': 

        st.header("Continental emissions since 1850")
        st.info("Select a continent from the menu")
        
        selected_continent = st.selectbox('Select country or group',continents)

        df = df_continents[df_continents['Entity'] == selected_continent]
        fig2 = px.line(df,"Year","Annual CO₂ emissions")
        st.plotly_chart(fig2)

    if chart == 'Comparing continents': 

        st.header("Continental emissions since 1850")
        st.info("To add a continet select it from the menu. You can also delete one, too")

        selected_continents = st.multiselect('Select country or group',continents,continents)

        df = df_continents[df_continents['Year'] >= 2010]
        df = df[df_continents['Entity'].isin(selected_continents)]

        fig3 = px.bar(df,"Year","Annual CO₂ emissions",color="Entity", barmode='group')
        st.plotly_chart(fig3)




