# Streamlit from Scratch: Presenting Data

## From text and tables to sophistcated charts. From Pandas dataframes, to Matplotlib, Plotly, Altair and other charts. Streamlit provides a comprehensive set of tools for presenting your data

TK add image

Streamlit was designed for Data Scientists and so data presentation is fundamental to it.

In previous articles, I've looked at how to get started with Streamlit and how to include various forms of text, images, video and audio in a Streamlit application. Now we get to the nitty gritty of how to represent the data that you have painstakingly discovered, processed and analysed.

Streamlit supports several charting packages, like Plotly, Altair and Bokeh, as well as ways of textually presenting data. We will look at them all.

TK add image of grid of charts from the various packages

We are going to explore these various packages, as well as the built-in methods of data visualization that Streamlit provides.

I will be presenting snippets of code that you can copy. Additionally, the entire code will be available for download from my web site. I'll put a link at the end of the article and it should be live shortly after this article is published.

If you want to follow along with the coding the first thing you need to do include the Streamlit package.

```` Python
import streamlit as st
````
If you need a primer on how to get started with Streamlit and what tools you need, see the first article in this series,  _[Streamlit from Scratch: Getting Started](https://towardsdatascience.com/streamlit-from-scratch-getting-started-f4baa7dd6493)_.

### Data

We are going to use two small data sets. The first is real cryptocurrency data for this year to date (Nov. 2022) ans the second is some fictional sales data. 

There is no formal source for the crypto data, I just Googled the value in USD of Bitcoin and Ethereum for the first day of each month this year, so far (Jan to Nov, 2022) and I invented the sales data for this article.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/data-tables.png)

To create this data, execute the following code.

```` Python
# Crypto monthly data
d = {'Month':[1,2,3,4,5,6,7,8,9,10,11],
     'Bitcoin':[47733,38777,44404,46296,38471,29788,19247,23273,20146,19315,20481],
     'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

cryptodf = pd.DataFrame(data = d)

# The Incredible Widget Company
d = {'Quarter':[1,2,3,4],
     'Widgets':[100,110,112,120],
     'Wodgets':[50,100,120, 125],
     'Wudgets':[200,150,100,90]}
     
salesdf = pd.DataFrame(d)
````

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

You can also display data as a _table_ or a _dataframe_. 

Tables are easily interpreted by readers as they are so ubiquitous. Run your finger down the rows until you find the one you are interested in and then run it across until you find the correct column.

On the face of it there doesn't seem to be much difference between the two; they both display a table. However ``st.dataframe()`` is more flexible. 

Both can take a Pandas dataframe as the source of the data but ``st.table()`` has no options, it simple displays the data in a table that fits the page (or container). ``st.dataframe()`` is more flexible, you can specify the height and width, or fill the width of the container and if the dataframe is too large it will be scrollable. ``st.dataframe()`` is also interactive - click on a cell and it will be highlighted; click on a column and the data will be ordered by that column.

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

Tables provide easy access to data if you know what you are looking for. But it is not particulary easy to detect trends or correlations.

For that you need charts.

## Charts

Streamlit supports several charting packages and also has three built-in charts that are essentially wrappers around their equivalent _Altair_ charts.

We'll look at the built-in ones first and then explore the other supported packages.

### Streamlit charts

The built-in charts are ``st.line_chart()``, ``st.bar_chart()`` and ``st.area_chart()``. They are attractive and easy to use but not very flexible - you need to explore one of the other supported packages for that.

Here is a line chart that shows the decline of Bitcoin and Ethereum over most of 2022.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.line-btc-eth.png)

```` Python
st.line_chart(df, x='Month')
````

The built-in charts require a data source, ``df`` and a data column to use as the x-axis. If the y-axis is left undefined then all of the remaining columns will be plotted. Otherwise, the y-axis should be a single column name, or a list of column names.

Here is a bar chart of the same Bitcoin data.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.bar-btc.png)

```` Python
st.bar_chart(df, y = 'Bitcoin', x='Month')
````

I have only plotted one column, here, because the default behaviour of this chart is to plot a stacked bar chart which means that we are adding one or more sets of values in order to construct the bar. 

This would be entirely suitable for a sales chart where individual items can be accumulated to form a total. Like this one that tracks the sales of items manufactured by the _The Formidable Widget Company_ over a year. Their flagship product is the _Widget_ but they have two other products, the _Wodget_ and the _Wudget_ and we can see how well they are selling, below.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/widget-sales-bar.png)

From this chart we can see that overall sales are not improving despite the apparent popularity of _Wodgets_. Sales of _Widgets_, their staple product, are holding up but the decline in the sales of _Wudgets_ is letting the company down badly.

Here is the code for that chart.

````Python
sales = pd.DataFrame(
     {'Quarter':[1,2,3,4],
      'Widgets':[100,110,112,120],
      'Wodgets':[50,100,120, 125],
      'Wudgets':[200,150,100, 90]})

st.bar_chart(sales, x='Quarter')
````
Notice that the y-axis is not defined, so all columns are plotted.

The last built-in chart is the area chart. Here are the sales data again.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/widget-sales-area.png)

````Python
st.area_chart(sales, x='Quarter')
````
Here you can see the relative performance of the sales lines, although in the area chart they not additive, so we do not easily get a view of the overall sales performance.

I have to say, I am not a great fan of this default colour scheme.

### Pyplot

The first supported charting package we will look at is _Pytlot_ - essentially this is support for the Python Matplotlib package but we can also use the Pandas plotting methods.

Here is a the code for a line plot of the crypto data.

```` Python
fig, ax = plt.subplots()
plt.plot(df['Bitcoin'])
st.pyplot(fig)
````

The first line of the code initializes the figure, ``fig``, and axis, ``ax``, variables. In this example ``ax`` is not used but we must initialize ``fig`` so that we can pass it to the ``st.plot()``.

This is the resuting chart.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/pyplot-line-basic-btc.png)

It's pretty basic but we can customize it with some additional commands. Here we add labels to the axes, a title and draw y-axis grid lines on a bar chart.

```` Python
# Pyplot charts are customizable
fig, ax = plt.subplots()
plt.bar(df.Month, df.Bitcoin)
ax.set_ylabel("Value in dollars")
ax.set_xlabel("Month 2022")
ax.set_title("Bitcoin")
plt.grid(axis='y')
st.pyplot(fig)
````

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/pyplot-bar-labels-btc.png)

This is better. Matplotlib charts are highly cutomizable but to get them exactly how you want them, you could end up writing quite a lot of code.

A compromise is to use the plotting methods from Pandas which will provide a slightly more sophisticated chart with the minimum of coding.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/pandas-plot-bar-btc-eth.png)

```` Python
fig, ax = plt.subplots()
df.plot.bar(x = 'Month', y=['Bitcoin','Ethereum'],ax=ax)
st.pyplot(fig)
````

Notice that here we can easily plot both BTC and ETH by specifiying them in a list. It is also important to note that we need to pass ``ax`` to the plot function call - in this way the new plot is added to the figure.

### Plotly

### Vega-lite

Vega-Lite is a grammar of graphics specification for interactive visualizations. It is platform neutral and you specify a Vega-lite graphic as a JSON structure.

We are not going to deal with Vega-Lite directly here because Altair is an  implementation of Vega-Lie in Python.

For more information on the specification, please refer to the [Vega-Lite website](http://vega.github.io/vega-lite/).

### Altair

As just mentioned, Altair charts are based on the Vega-Lite specification, so the graphics produced by Altair will be the same as Vega-Lite.



### Bokeh

### Conclusion