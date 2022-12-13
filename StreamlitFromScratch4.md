# Streamlit from Scratch: Build a Dashboard with Streamlit's Layout and UI features

## Streamlit has simple but effective components for user interaction and layout which let us build effective and attractive dashboard applications

TK image

We are going to explore some of the layout and user interface features of Streamlit so as to create a simple but effective dashboard app. In previous articles in this series, we have seen how to present text, media and data, now we use this knowledge and add layout and user interface components to create a complete application.

TK image of app(s)

Streamlit tries to make life simple for the app developer and so does not have the vast number of UI options that are available in other technologies such as HTML and Javascript UI libraries. But using its layout components you can easily design an attractive and capable web page.

A Streamlit app is constructed with various container elements and user interface components such as a slider and select boxes, and we will look a a few of them.

But first we need some data to work with.

The code below gets four data files from my Github repository [CO2](https://github.com/alanjones2/CO2). They contain data on world-wide carbon dioxide emissions over the last couple of hundred years. The original data comes from Our World in Data[1] and I have simply broken that down into four different subsets. The first contains data for each country in the world, the second breaks it down by continent, the third is for the whole world and the last one represents groups of countries by income type.

I've also included all of the libraries that we will use in this article.

## Fetch the data and cache it

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

You may wonder why I've written functions to download and create a dataframe for each of the files. The reason for this is indicated by the Python decorator ``@st.cache``.

Whenever the user interacts with a Streamlit app, to enter a value, or change a setting, for example, the entire Streamlit app is re-run from the beginning. This may appear to be inefficient but it is the way that Streamlit works and doesn't normally impact the user experience too badly.

Except that there are occasions when it does and that impact could be significant.

If a lot of data is downloaded from an external source, this will take time. And while this maybe acceptable when the app first starts up, you don't really want a long pause in the middle of the user changing something. And this is what the ``@st.cache`` decorator is all about. 

Marking a function in this way tells Streamlit to cache any resulting data and stops the function being called again unless the parameters passed to it have changed. Instead the cached data is returned to the caller.

In our functions there are no parameters and so the the functions will only ever be called once. This is exactly what we want as the data is not going to change and so it will only be fetched the first time the functions are called and, thereafter, the cached data will be used.

The dataframes all look something like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/co2-table-countries.png)


They contain columns for the 
- _Entity_: country, continent, income group or 'World'
- _Code_: the ISO country code (if it is a country)
- _Year_
- _Annual CO2 Emissions_: from burning fossil fuel and industrial processes
- _Annual CO2 Emissions including land-use change_: the sum of the previous column and next one
- _Annual CO2 Emissions from land-use change_

We'll be using the first four columns in each table to show the emissions over time for each of the entity-types.

Our first focus will be the World. We'll show the how emissions have changed in all countries of the world on a map. The user will select a year and the countries will be shaded according to the level of their emissions.

This is where we come across our first Streamlit UI component. We will use a slider to allow the user to select a year.

## Sliders

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


Here is the code. There is nothing particularly difficult in creating the choropleth. Plotly does all the hard work for you, we just have to provide the appropriate values.

```` Python
max = df_countries['Annual CO₂ emissions'].max()

year = st.slider('Select year',1850,2020)
fig1 = px.choropleth(df_countries[df_countries['Year']==year], locations="Code",
                    color="Annual CO₂ emissions",
                    hover_name="Entity",
                    range_color=(0,max),
                    color_continuous_scale=px.colors.sequential.Blues)
st.plotly_chart(fig1)
````

In the code we have used the value of ``year`` to filter the dataframe and that is the data that the choropleth will use. We have also calculated the maximum value of CO2 emissions in tha table and this is used to set the range of colours that will be used on the map. In addition to the data, the other parameters are:

- ``locations``: the ISO codes that will be used to identify areas on the map
- ``color``: the value that wil be used to set the colour
- ``hover_name``: the string that will be shown when hovering over the map, i.e. the country name
- ``range_color``: the range of values that will be mapped onto the colours
- ``color_continuous_scale``: the list of colours that will be used (in this case a range of continuous blues provided in Plotly Express)

The detail of this figure is a little difficult to see but if you use the expander control (which expands the image to fullscreen) and/or the zoom facility individual countries can be easily seen.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/choropleth-full-screen.png)

Sliders can also be used for categorical values and these also support a range. For example:

```` Python
start_month, end_month = st.select_slider(
    'Select a range of months',
    options=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    value=('Jan', 'Dec'))
    
st.write('You selected months between', start_month, 'and', end_month)
````

This lets the user select the beginning and end of a list of months with the default result being 'Jan' and 'Dec'. Here is the result:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/select_slider.png)

## Select boxes

Streamlit provides two _selectbox_ methods: one for selecting a single item and another for selecting multiple items.

Below is an example of the single _selectbox_. It let's you select a continent and shows the CO2 emissions for that continent as a line graph. First, we need to create a list of continents and store that in ``continents`` then we see the _selectbox_ which will let the user choose a continent. Using that value we filter the dataframe and plot a line chart with Plotly.

```` Python
continents = df_continents['Entity'].unique()

selected_continent = st.selectbox('Select country or group',continents)

df = df_continents[df_continents['Entity'] == selected_continent]

fig2 = px.line(df,"Year","Annual CO₂ emissions")

st.plotly_chart(fig2, use_container_width=True)
````
The result looks like this.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/single_select_box_continents.png)

Clicking in the field that displays the continent will bring down a menu from which other values can be selected.

If we want to run something similar but where we can compare countries then the _muliple selectbox_ is what we need.

Here is a similar function that uses ``st.multiselect()``. This lets the user select from a drop-down menu in a similar way but once selected the value is kept in a list which is displayed in box above the menu. To remove an item from the list you click _x_ for that item and it will reappear in the menu.

The code is very similar to the previous function except that instead of filtering the dataframe on a single value, we use the ``isin()`` method to check if the continent name is in the selected list. I've also restricted the number of years so that the figure is more readable.

````Python
continents = df_continents['Entity'].unique()

selected_continents = st.multiselect('Select country or group',
                                      continents, continents)
df = df_continents[df_continents['Year'] >= 2010]
df = df[df_continents['Entity'].isin(selected_continents)]

fig = px.bar(df,"Year","Annual CO₂ emissions",color="Entity", barmode='group')
st.plotly_chart(fig, use_container_width=True)
````
Here is the result with five continents selected.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/multiple_select_box_continents.png)


## Radio buttons

The next UI component that we will look at is one that implemements radio buttons.

The code should look familiar, first a propmpt and then a list of items that can be selected. Following this is a set of ``if`` statements that test the value of ``chart`` and display the correct chart from the ones that we created earlier.

```` Python
chart = st.radio(
    "Select the chart that you would like to display",
    ('World Map', 'Continent Emissions', 'Comparing continents'))

if chart == 'World Map': 
    st.plotly_chart(fig1)
if chart == 'Continent Emissions': 
    st.plotly_chart(fig2)
if chart == 'Comparing continents': 
    st.plotly_chart(fig3)
````

The result looks like this.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/radio_button_example.png)

## Layout

There are several other UI components that Streamlit provides but we'll leave it at that for now because in order to construct an effective app, we need to know how to layout the components that we have seen so far.

We'll now turn our attention to layout. Streamlit provides a number of layout elements, containers, columns and a sidebar. We are going to use these features to construct two versions of a dashboard application based on the data that we have been looking at.

However, before we start let's look at the two methods of using layput components - object notation and ``with``.

### Using object notation or ``with:``

Layout components can be programmed using object notation or with the ``with:`` keyword. Here is a piece of fictional code that shows the difference.

```` Python
# Object notation
layoutcomponent1.write('This will be written inside component 1')
layoutcomponent1.write('This will also be written inside component 1')

# 'with' notation
with layoutcomponent2:
    st.write('This will be written inside component 2')
    st.write('This will also be written inside component 2')
````

Both of these examples work in the same way and produce the same results.

With object notation, the name of the layout object replaces ``st`` so where you might write ``st.write("stuff")`` to write something that is not contained in a layout component, when writing inside such a component you replace ``st`` with the component name.

When using ``with`` notation you open a block using ``with component_name``. Anything written inside the block is displayed in the layout component and the normal ``st`` prfix is used.

 Using ``with:`` lets you group the operations on the layout component together, whereas object notation gives you the freedom to scatter those operation throughout the code. It's entirely up to you to decide which to use but I tend to go for the ``with:`` option where possible - I think it is more rational to keep the code together in a block, if you can.

 If this is not entirely clear, it will become so when we deal with some concrete examples.

 Let's do just that.

## Sidebar

The sidebar was one of the first layout components that featured in Streamlit. This allows you to group user input controls in an area to the side of the screen and display the rest of the app in the main window.

Here is a simple illustration of how it can be used. The sidebar contains three radio buttons that let you select one of three images to be displayed in the main window. (Note that for simplicity, these are static images of charts we created earlier. You could, of course, put any code in the ``if`` blocks, including the code that we previously used to create the interactive charts.)

```` Python
import streamlit as st

# The title will be displayed at the top of the main window
st.title('Demonstration of the sidebar')

# Everything in the 'with' block will be in the sidebar
with st.sidebar:
    st.header('Select an image to be displayed')
    chart = st.radio(
    "Select the image that you would like to display",
    ('World Map', 'Continent Emissions', 'Comparing continents'))

# The following is outside of the 'with' block and so will 
# execute in the main window
if chart == 'World Map': 
    st.image('../images/choropleth.png')

if chart == 'Continent Emissions': 
    st.image('../images/single_select_box_continents.png')

if chart == 'Comparing continents': 
    st.image('../images/multiple_select_box_continents.png')
````
And this is what it looks like.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/sidebar_example.png)

As you can see this is a very conventional layout - simple and effective. Note that the sidebar can be closed with the _x_ in the top right corner. It can, of course be re-opened.

## Columns


```` Python
#
# Code to import libraries and get the data goes here
#

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

        # code to draw the choropleth

    if chart == 'Continent Emissions': 
        
        # code to draw a bar chart

    if chart == 'Comparing continents': 

        # code to draw the multiple bar chart
````

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/sidebar_app.png)








---

### Notes

[1] [Our World in Data](https://ourworldindata.org/) is a treasure trove of information whose mission is to publish _“research and data to make progress against the world’s largest problems”_. All of their work is made available under the [Creative Commons BY license](https://creativecommons.org/licenses/by/4.0/).