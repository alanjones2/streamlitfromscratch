import streamlit as st

st.title('Demonstration of the sidebar')

with st.sidebar:
    st.header('Select an image to be displayed')
    chart = st.radio(
    "Select the chart that you would like to display",
    ('World Map', 'Continent Emissions', 'Comparing continents'))

if chart == 'World Map': 
    st.image('../images/choropleth.png')

if chart == 'Continent Emissions': 
    st.image('../images/single_select_box_continents.png')

if chart == 'Comparing continents': 
    st.image('../images/multiple_select_box_continents.png')
