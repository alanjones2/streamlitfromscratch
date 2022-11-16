import streamlit as st
import pandas as pd
import altair as alt

st.title("Presenting data in Streamlit")

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

d = {'Month':[1,2,3,4,5,6,7,8,9,10,11],
     'Bitcoin':[47733,38777,44404,46296,38471,29788,19247,23273,20146,19315,20481],
     'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

df = pd.DataFrame(data = d)




st.markdown("### Display a dataframe with ``st.table()``")

st.table(df)

st.markdown('---')

st.markdown("### Display a dataframe with ``st.dataframe()``")

st.dataframe(df)

st.markdown('---')

st.markdown("### Built-in charts ``st.line_chart()``, ``st.bar_chart()`` and ``st.area_chart()``")

st.line_chart(df, x='Month')
st.line_chart(df, y = 'Ethereum', x = 'Month')
st.bar_chart(df, y = 'Bitcoin', x='Month')
st.area_chart(df, y = 'Bitcoin', x = 'Month')

st.markdown('---')

st.markdown('### Built-in charts are not very flexible')
st.markdown('#### but there are plenty of others to choose from')


st.markdown('### PyPlot Charts')
st.write("This is used for all Matplotlib-based charting libraries")

import matplotlib.pyplot as plt

# Note that explicitly initialising fig and ax are required by Streamlit because 
# # a figure object must be passed to st.pyplot() 
fig, ax = plt.subplots()

plt.plot(df)
st.pyplot(fig)

fig, ax = plt.subplots()

# Pyplot charts are customizable
plt.bar(df.Month, df.Bitcoin)
ax.set_ylabel("Value in dollars")
ax.set_xlabel("Month 2022")
ax.set_title("Bitcoin")
plt.grid(axis='y')
st.pyplot(fig)

st.markdown('---')

st.markdown('### Here are a couple of Altair charts:')

df = pd.DataFrame(d)

c = alt.Chart(df).mark_line().encode(
    x='Month:O', y='Bitcoin')

st.altair_chart(c, use_container_width=True)

c = alt.Chart(df).mark_bar().encode(
    x='Month:O', y='Bitcoin')

st.altair_chart(c, use_container_width=True)