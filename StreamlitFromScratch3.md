## Streamlit from Scratch: Presenting Data

### From text and tables to sophistcated charts. From Pandas dataframes, to Matplotlib, Plotly, Altair and other charts. Streamlit provides a comprehensive set of tools for presenting your data



Streamlit was designed for Data Scientists and so data presentation is fundamental to it.

In previous articles, I've looked at how to get started with Streamlit and how to include various forms of text, images, video and audio in a Streamlit application. Now we get to the nitty gritty of how to represent the data that you have painstakingly discovered, processed and analysed.

We are going to explore various ways of data visualization and I will be presenting snippets of code that you can copy. Additionally, the entire code will be available for download from my web site. I'll put a link at the end of the article and it should be live shortly after this article is published.

If you want to follow along with the coding the first thing you need to do include the Streamlit package.

```` Python
import streamlit as st
````
A full description of how to get started and what tools you need is in my article _[Streamlit from Scratch: Getting Started](https://towardsdatascience.com/streamlit-from-scratch-getting-started-f4baa7dd6493)_.

### Text and tables

We will get to Streamlit's charting capabilities shortly but presenting data is not always about charts. Sometimes a simple textual presentation or a table is a perfectly adequate way of getting your message across. 

Streamlit provides a neat way of presenting a simple change in a value, ``st.metric()``. It looks like this

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/metric-bitcoin.png)

and is very easy to construct.

```` Python

btcCurrent = 16080
btcYrBeg = 47733
btcdelta = btcCurrent - btcYrBeg
st.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
          help="Change in Bitcoin dollar value since the year beginning")

````

