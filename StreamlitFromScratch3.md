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

### Data

A recent comment from someone on Twitter went something like "Who'd have thought that something that has no instrinsic value would end up being worthless?". 

Yes, we are going to use data about cryptocurrencies to demonstrate Streamlit's data visualization capabilities.

There is no formal source for this data, I just Googled the value in USD of Bitcoin and Ethereum for the first day of each month this year, so far (Jan to Nov, 2022).

### Text and tables

We will get to Streamlit's charting capabilities shortly but presenting data is not always about charts. Sometimes a simple textual presentation or a table is a perfectly adequate way of getting your message across. 

Streamlit provides a neat way of presenting a simple change in a value, ``st.metric()``. It looks like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/metric-bitcoin.png)

_Image by author_

It is very easy to construct. The code below uses ``st.metric()`` to diplay the change in value of Bitcoin (BTC) since the beginning of this year. I start by defining 3 variables, ``btcCurrent``, the value of BTC at the time of writing, ``btcYrBeg``, the value at the beginning of the year, and ``btcDelta``, the change from then until now.

```` Python
btcCurrent = 16080
btcYrBeg = 47733
btcdelta = btcCurrent - btcYrBeg

st.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
          help="Change in Bitcoin dollar value since the year beginning")
````

TK how it works

I've done much the same thing with Ethereum (ETH) and then combined the two _metrics_ with some text into three columns to provide a simple but effective presentation.

It looks like this:
![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/metric-btc-eth.png)

_Image by author_

Here is the code:

```` Python
ethCurrent = 1225
ethYrBeg = 3767
ethdelta = ethCurrent - ethYrBeg

# Use columns to display them together
col1, col2, col3 = st.columns([50,25,25])
col1.write("The value of crytocurrencies has dropped considerably since the beginning of the year")
col2.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
            help="Change in Bitcoin dollar value since the year beginning")
col3.metric("Ethereum", ethCurrent, delta=ethdelta, delta_color="normal", 
            help="Change in Ethereum dollar value since the year beginning")
````

TK how the columns work


You can also display data as a table or a dataframe. On the face of it there doesn't seem to be much difference between the two; they both display a table. However ``st.dataframe()`` is more flexible. Both take a Pandas dataframe (for example) as the source of the data but ``st.table()`` has no options, it simple displays the data in a table that fits the page (or container). ``st.dataframe()`` is more flexible, you can specify the height and width, or fill the width of the container and if the dataframe is too large it is scrollable. ``st.dataframe()`` is also interactive - click on a cell and it will be highlighted; click on a column and the data will be ordered by that column.

Here is a table that displays a monthly view of BTC and ETH prices.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/table-btc-eth.png)

_Image by author. Data source: Google_
````Python
d = {'Month':[1,2,3,4,5,6,7,8,9,10,11],
     'Bitcoin':[47733,38777,44404,46296,38471,29788,19247,23273,20146,19315,20481],
     'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

df = pd.DataFrame(data = d)

st.table(df)
````

And here is the dataframe version that has a highlighted cell.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/df-btc-eth.png)

_Image by author. Data source: Google_

I've kept it the same width as the table by setting the ``use_container_width`` parameter to ``True``.

````Python
st.dataframe(df, use_container_width= True)
````

### Charts

Streamlit supports several charting packages and also has three built-in charts that are essentially wrappers around the equivalent _Altair_ charts.

The built-ins are ``st.line_chart()``, ``st.bar_chart()`` and ``st.area_chart()``. They are attractive and easy to use but not very flexible - you need to explore one of the other supported packages for that.

Here is a line chart that shows the drastic decline of Bitcoin and Ethereum over the last few months.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.line-btc-eth.png)

```` Python
st.line_chart(df, x='Month')
````

In each case the built-in charts require a data source, ``df`` and a column to use as the x-axis. If the y-axis is left undefined then all of the remaing columns will be plotted. Otherwise, the y-axis should be a single column name, or a list of column names.

Here is a bar chart of the same Bitcoin data.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.bar-btc.png)

I have only plotted one column, here, because the default behaviour of this chart is to plot a stacked bar chart.


![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.area-btc.png)

TK expand this: bar charts are stacked, y axis is one of: one column, a list of columns, all remaining columns (None)