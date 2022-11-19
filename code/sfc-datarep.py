#################################################
# Data presentation in Streamlit
#
# MIT License
#
# Copyright (c) 2022 Alan Jones - see LICENCE.md
#

import streamlit as st
import pandas as pd
import altair as alt

st.title("Presenting data in Streamlit")

### set up the data

st.markdown("### Set up some data")


# Crypto monthly data
d = {'Month':[1,2,3,4,5,6,7,8,9,10,11],
     'Bitcoin':[47733,38777,44404,46296,38471,29788,19247,23273,20146,19315,20481],
     'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

cryptodf = pd.DataFrame(data = d)

# The Original Widget Company
d = {'Quarter':[1,2,3,4],
     'Widgets':[100,110,112,120],
     'Wodgets':[50,100,120, 125],
     'Wudgets':[200,150,100,90]}
     
salesdf = pd.DataFrame(d)

col1, col2 = st.columns(2)
col1.info("Crypto currencies, Jan to Nov. 2022")
col1.table(cryptodf)
col2.info("Sales for the Incredible Widget Company")
col2.table(salesdf)

st.markdown('---') 

### st.metric()

# Bitcoin value at the beginning of the year and now 
st.markdown("### Using ``st.metric()`` we can display a neat textual representation of a change in value")

btcCurrent = 16080
btcYrBeg = 47733
btcdelta = btcCurrent - btcYrBeg
st.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
          help="Change in Bitcoin dollar value since the year beginning")

st.markdown('---')

# Ethereum value at the beginning of the year and now 
ethCurrent = 1225
ethYrBeg = 3767
ethdelta = ethCurrent - ethYrBeg
st.metric("Ethereum", ethCurrent, delta=ethdelta, delta_color="normal", 
          help="Change in Ethereum dollar value since the year beginning")

st.markdown('---')

st.markdown("### Combining ``st.metric()`` with text in columns:")

# Use columns to display them together
col1, col2, col3 = st.columns([50,25,25])
col1.write("The value of crytocurrencies has dropped considerably since the beginning of the year")
col2.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
            help="Change in Bitcoin dollar value since the year beginning")
col3.metric("Ethereum", ethCurrent, delta=ethdelta, delta_color="normal", 
            help="Change in Ethereum dollar value since the year beginning")

st.markdown('---')

st.markdown("### Display a dataframe with ``st.table()``")

st.table(cryptodf)

st.markdown("### Display a dataframe with ``st.dataframe()``")

st.dataframe(cryptodf, use_container_width= True)

st.markdown('---')

### Streamlit charts

st.markdown("### Streamlit charts ``st.line_chart()``, ``st.bar_chart()`` and ``st.area_chart()``")

st.markdown("#### Built-in charts for the crypto data")

st.line_chart(cryptodf, x='Month')
st.bar_chart(cryptodf, x='Month')
st.warning("The bar chart doesn't do what we want - it shouldn't be stacked for this type of data")
st.area_chart(cryptodf, x='Month')

st.markdown("#### Built-in charts for Bitcoin data, only")

st.line_chart(cryptodf, y = 'Bitcoin', x = 'Month')
st.bar_chart(cryptodf, y = 'Bitcoin', x='Month')
st.area_chart(cryptodf, y = 'Bitcoin', x = 'Month')

st.markdown("#### Some made-up sales data shows a use of the built-in bar chart")

# A stacked bar chart of sales figures
st.bar_chart(salesdf, x='Quarter')
st.area_chart(salesdf, x='Quarter')

st.markdown('---')

st.info("""### Built-in charts are not very flexible
but there are plenty of others to choose from""")

### Pyplot

st.markdown('### PyPlot Charts')
st.write("This is used for Matplotlib-based charts so we can use it for Pandas plots, too")

import matplotlib.pyplot as plt

# Note that explicitly initialising fig and ax are required by Streamlit because 
# # a figure object must be passed to st.pyplot() 
fig, ax = plt.subplots()

plt.plot(cryptodf['Bitcoin'])
st.pyplot(fig)

# Pyplot charts are customizable
fig, ax = plt.subplots()
plt.bar(cryptodf.Month, cryptodf.Bitcoin)
ax.set_ylabel("Value in dollars")
ax.set_xlabel("Month 2022")
ax.set_title("Bitcoin")
plt.grid(axis='y')
st.pyplot(fig)

st.markdown('---')

st.markdown("### Here are some Pandas plotted charts")
fig, ax = plt.subplots()
cryptodf.plot.bar(x = 'Month', y=['Bitcoin','Ethereum'],ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
salesdf.plot.bar(x = 'Quarter', y=['Widgets','Wodgets','Wudgets'],stacked = True, ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
salesdf.plot.area(x = 'Quarter', y=['Widgets','Wodgets','Wudgets'],ax=ax)
st.pyplot(fig)

st.markdown('---')

### Altair

st.markdown('### Here are some Altair charts:')

st.write("First a line and bar chart for Bitcoin performance")

c = alt.Chart(cryptodf).mark_line().encode(
    x='Month:O', y='Bitcoin')

st.altair_chart(c, use_container_width=True)

c = alt.Chart(cryptodf).mark_bar().encode(
    x='Month:O', y='Bitcoin')

st.altair_chart(c, use_container_width=True)

st.write("To compare more than one value, it's easier to transform the data")
cryptodf1 = pd.melt(cryptodf, 
              value_vars=['Bitcoin','Ethereum'], 
              id_vars=['Month'],
              var_name='Name'
              )
salesdf1 = pd.melt(salesdf, 
              value_vars=['Widgets','Wodgets','Wudgets'], 
              id_vars=['Quarter'],
              var_name='Name'
              )
col3,col4 = st.columns(2)
col3.table(cryptodf1)
col4.table(salesdf1)

st.info("A grouped bar chart for crypto")
c = alt.Chart(cryptodf1).mark_bar().encode(
    x='Name:O', 
    y='value:Q', 
    color = 'Name:N', 
    column = 'Month:N')

st.altair_chart(c, use_container_width=False)

st.info("A grouped bar chart for sales")
c = alt.Chart(salesdf1).mark_bar().encode(
    x='Name:O', 
    y='value:Q', 
    color = 'Name:N', 
    column = 'Quarter:N')

st.altair_chart(c, use_container_width=False)

st.info("A line chart for sales")

c = alt.Chart(salesdf1).mark_line().encode(
    x='Quarter', 
    y='value', 
    color = 'Name:N'
    )

st.altair_chart(c, use_container_width=False)

st.info("A line chart for crypto")

c = alt.Chart(cryptodf1).mark_line().encode(
    x='Month', 
    y='value', 
    color = 'Name:N'
    )

st.altair_chart(c, use_container_width=False)

# scatter plot using circles
c = alt.Chart(salesdf1).mark_circle().encode(
    x='Quarter', 
    y='value', 
    color = 'Name'
    )

st.altair_chart(c, use_container_width=False)

