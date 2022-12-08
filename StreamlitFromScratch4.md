## Streamlit from Scratch: Build a Dashboard with Streamlit's Layout and UI features

### Streamlit has simple but effective components for user interaction and layout which let us build effective and attractive dashboard applications

TK image

We are going to explore the layout and user interface aspects of Streamlit so as to create a simple but effective dashboard app. In previous articles in this series, we have seen how to present text, media and data, now we use this knowledge and add layout and user interface components to create a complete application.

TK image of app

Streamlit tries to make life simple for the app developer and so does not have the vast number of UI options that are available in other technologies such as HTML and Javascript UI libraries. But using its layout components you can easily design an attractive and capable web page.

A Streamlit app is constructed with various container elements and user interface components such as a slider and select boxes, and we will look a a few of them.

But first we need some data to work with.

The code below gets four data files from my Github repository [CO2](https://github.com/alanjones2/CO2). They contain data on world-wide carbon dioxide emissions over the last couple of hundred years. The original data comes from Our World in Data[1] and I have simply broken that down into four different subsets. The first contains data for each country in the world, the second breaks it down by continent, the third is for the whole world and the last one represents groups of countries by income type.

I've also included all of teh libraries that we will use in this article.

## Get the data

````Python
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

df_countries= get_countries_data()
df_continents= get_continent_data()
df_world = get_world_data()
df_groups = get_group_data()
````

TK Explain caching

You may think that I have gone a little over the top in writing functions to download and create a dataframe for each of the files. There is a reason for this and this is indicated by the Python decorator ``@st.cache``.

Whenever the user interacts with a Streamlit app, to enter a value, or change a setting, for example, the entire Streamlit app is re-run from the beginning. This may appear to be inefficient but it is the way that Streamlit works and doesn't really impact too much on the use experience.

Except that there are occasions when it does and that imapact could be significant.

If a lot of data is downloaded from an external source, this will take time. And while this maybe acceptable when the app first starts up, you don't really want a long pause in the middle of the user changing something. And this is what the ``@st.cache`` decorator is all about. 

Marking a function in this way tells Streamlit to cache any resulting data and stops the function being called again unless the parameters passed to it have changed. Instead the cached data is returned to the caller.

In our functions there are no parameters and so the the functions will only ever be called once. This is exactly what we want as the data is not going to change and so the data will only be fetched the first time the functions are called and, thereafter, the cached data will be used.

The dataframes look like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/co2-table-countries.png)
)

They contain columns for the 
- _Entity_: country, continent, income group or 'World'
- _Code_: the ISO country code (where applicable)
- _Year_
- _Annual CO2 Emissions_: from burning fossil fuel and industrial processes
- _Annual CO2 Emissions including land-use change_: the sum of the previous column and next one
- _Annual CO2 Emissions from land-use change_

We'll be using the first four columns in each table to show the emissions over time for each of the entity-types.

Our first focus will be the World. We'll show the how emissions have changed in all countries of the world on a map. The user will select a year and the countries will be shaded according to the level of their emissions.

This is where we come across our first Streamlit UI component. We will use a slider to allow the user to select a year.

### Sliders

Sliders are very easy to use:

```Python
year = st.slider('Select year',1850,2020)
````

The ``st.slider`` method requires three parameters, a prompt string and two numerical limits. The return value is a value between the limits corresonding to the position of the slider. In the image below the range is between 1850 and 2020 and the return value will be 1978.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/slider.png)

Remember that when a UI control changes, the whole of the app is re-run. Only when the slider is moved will the return value be updated.

A fourth parameter can be given to set a default value for the slider, e.g.

```Python
year = st.slider('Select year',1850,2020,1950)
````
We are going to use the year value in a Plotly choropleth which will give us a figure like this one, below.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/choropleth.png)

The detail of this figure is a little difficult to see but if you use the expander control (which exanps the image to fullscreen) and/or the zoom facility individual countries can be easily seen.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/choropleth-full-screen.png)

Here is the code. There is nothing particularly difficult in creating the choropleth. Plotly does all the hard work for you, we just have to provide the appropriate values.

```` Python
def map():
    max = df_countries['Annual CO₂ emissions'].max()

    year = st.slider('Select year',1850,2020)
    fig = px.choropleth(df_countries[df_countries['Year']==year], locations="Code",
                        color="Annual CO₂ emissions",
                        hover_name="Entity",
                        range_color=(0,max),
                        color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig, use_container_width=True)
````
The code is written as a function because this will make it clearer when we re-use it in later examples. You run it like this (of course):

```` Python
map()
````

In the code we have used the value of ``year`` to filter the dataframe and that is the data that the choropleth will use. We have also calculated the maximum value of CO2 emissions in tha table and this is used to set the range of colours that will be used on the map. In addition to the data, the other parameters are:

- ``locations``: the ISO codes that will be used to identify areas on the map
- ``color``: the value that wil be used to set the colour
- ``hover_name``: the string that will be shown when hovering over the map, i.e. the country name
- ``range_color``: the range of values that will be mapped onto the colours
- ``color_continuous_scale``: the list of colours that will be used (in this case a range of continuous blues provided in Plotly Express)

````Python
def continents_bar_graph():

    continents = df_continents['Entity'].unique()

    selected_continents = st.multiselect('Select country or group',
                                          continents, continents)

    df = df_continents[df_continents['Year'] >= 2010]

    df = df[df_continents['Entity'].isin(selected_continents)]

    fig = px.bar(df,"Year","Annual CO₂ emissions",color="Entity", barmode='group')

    st.plotly_chart(fig, use_container_width=True)
````


---

### Notes

[1] [Our World in Data](https://ourworldindata.org/) is a treasure trove of information whose mission is to publish _“research and data to make progress against the world’s largest problems”_. All of their work is made available under the [Creative Commons BY license](https://creativecommons.org/licenses/by/4.0/).