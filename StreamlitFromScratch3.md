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

### Text

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

I've done much the same thing with Ethereum (ETH) and then combined the two _metrics_ with some text into three columns to provide a simple but effective presentation. Here is the code requred for Ethereum.

```` Python
ethCurrent = 1225
ethYrBeg = 3767
ethdelta = ethCurrent - ethYrBeg
````



Here is the code to display the data in columns:

```` Python
# Use columns to display them together
col1, col2, col3 = st.columns([50,25,25])
col1.write("The value of crytocurrencies has dropped considerably since the beginning of the year")
col2.metric("Bitcoin", btcCurrent, delta=btcdelta, delta_color="normal", 
            help="Change in Bitcoin dollar value since the year beginning")
col3.metric("Ethereum", ethCurrent, delta=ethdelta, delta_color="normal", 
            help="Change in Ethereum dollar value since the year beginning")
````
The result looks like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/metric-btc-eth.png)

_Image by author_

TK how the columns work


### Tables and dataframes

You can also display data as a _table_ or a _dataframe_. 

Tables are easily interpreted by readers as they are so ubiquitous. Run your finger down the rows until you find the one you are interested in and then run it across until you find the correct column and there is the figure you are looking for!

On the face of it there doesn't seem to be much difference between the two methods; they both display a table. However ``st.dataframe()`` is more flexible. 

Both can take a Pandas dataframe as the source of the data but ``st.table()`` has no other options, it simple displays the data in a table that fits the page (or container). ``st.dataframe()`` is more flexible, you can specify the height and width, or fill the width of the container and if the dataframe is too large it will be scrollable. ``st.dataframe()`` is also interactive - click on a cell and it will be highlighted; click on a column and the data will be ordered by that column.

Here is a table that displays a monthly view of BTC and ETH prices.

````Python
st.table(cryptodf)
````

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/table-btc-eth.png)

_Image by author. Data source: Google_


And here is the dataframe version that has a user highlighted cell.

````Python
st.dataframe(cryptodf, use_container_width=True)
````

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/df-btc-eth.png)

_Image by author. Data source: Google_

I've kept the dataframe the same width as the table by setting the ``use_container_width`` parameter to ``True``.

Tables provide easy access to data if you know what you are looking for. But it is not particulary easy to detect trends or correlations.

For that you need charts.

## Streamlit charts

Streamlit supports several charting packages and also has three built-in charts that are essentially wrappers around their equivalent _Altair_ charts.

We'll look at the built-in ones first and then explore the other supported packages.

The built-in charts are ``st.line_chart()``, ``st.bar_chart()`` and ``st.area_chart()``. They are attractive and easy to use but not flexible.

Here is a line chart that shows the decline of Bitcoin and Ethereum over most of 2022.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.line-btc-eth.png)

And here is the code that produced it. 

```` Python
st.line_chart(df, x='Month')
````

The built-in charts require a data source, ``df`` and a data column to use as the x-axis. If the y-axis is left undefined then all of the remaining columns will be plotted. Otherwise, the y-axis should be a single column name, or a list of column names.

Here is a bar chart of the just the Bitcoin data.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/st.bar-btc.png)

```` Python
st.bar_chart(df, y = 'Bitcoin', x='Month')
````

I have only plotted one column, here, because the default behaviour of this chart is to plot a stacked bar chart which means that we are adding one or more sets of values in order to construct the bar. 

This would be entirely suitable for a sales chart where individual items can be accumulated to form a total. Like this one that tracks the sales of items manufactured by the _The Incredible Widget Company_ over a year. Their flagship product is the _Widget_ but they have two other products, the _Wodget_ and the _Wudget_ and we can see how well they are selling, below. (We saw how to construct the data earlier.)

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/widget-sales-bar.png)

From this chart we can see that overall sales are not improving despite the apparent popularity of _Wodgets_. Sales of _Widgets_, their staple product, are holding up but the decline in the sales of _Wudgets_ is letting the company down badly.

Here is the code to produce that chart.

````Python
st.bar_chart(salesdf, x='Quarter')
````
Notice that the y-axis is not defined, so all columns are plotted.

The last built-in chart is the area chart. Here are the sales data again.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/widget-sales-area.png)

````Python
st.area_chart(salesdf, x='Quarter')
````
Here you can see the relative performance of the sales lines, although in the area chart they not additive, so we do not easily get a view of the overall sales performance.

I have to say, I am not a great fan of this default colour scheme.

### Pyplot

The first supported charting package we will look at is _Pyplot_ - essentially this is support for the Python Matplotlib package but we can also use the Pandas plotting methods as they are built on the Matplotlib package.

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

Vega-Lite is a platform neutral grammar of graphics specification for interactive visualizations. 

A Vega-Lite graphic is specified as a JSON structure, like this one from the Vaga-Lite examples web page.

```` JSON
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
````
[_Listing courtesy of the Vega-Lite examples web page_](https://vega.github.io/vega-lite/examples/line.html)

This also is a valid declaration for a Python list and so we can assign it to a variable and plot it like this.
````Python
st.vega_lite_chart(c)
````

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/vega-lite-bar.png)

To my mind this is a rather long-winded way of creating a graphic and because Altair is an  implementation of Vega-Lite in Python, we will pass on this particular feature of Streamlit and move on to Altair.

For more information on the Vega-Lite specification, please refer to the [Vega-Lite website](http://vega.github.io/vega-lite/).

### Altair

As just mentioned, Altair charts are based on the Vega-Lite specification, so the graphics produced by Altair will be the same as Vega-Lite.

To plot an altair chart we first need to import the library:
```` Python
import altair as alt
````

We then define a chart and use ``st.altair_chart(c)``, where ``c`` is the chart, to plot it.

The syntax to define an altair chart is quite different to what we have so far encountered. It is a declarative system and we start by defining a chart object.
```` Python
c = alt.Chart(cryptodf)
````
This creates a chart from the dataframe ``cryptodf`` but it doesn't do much for us as it is. We now need to declare _marks_ and _encodings_.

_Marks_ are how the chart should be visualized, they may be lines, points, bars, etc. E.g.

```` Python
c = alt.Chart(cryptodf).mark_line()
````

Means that we want to draw a line chart.

Then to visually make sense of the data we can map various encoding channels to columns in the dataset. 

We could encode the column ``'Month'`` of the data with the ``x`` channel, for example, which represents the x-axis position of the points. That gives us one axis. Then we could encode the column ``'Bitcoin'`` to the ``y``.

```` Python
c = alt.Chart(cryptodf).mark_line().encode(
    x='Month:O', y='Bitcoin')
````

The strange ``:O`` in the code tells Altair that ``'Month'`` is an ordinal value and so it will be displayed as a list of integers (otherwise they would be displayed as real number and representing _January_ with the number 1.0 is a bit odd).

To draw the chart we call the ``st.altair_chart()`` method:

```` Python
st.altair_chart(c, use_container_width=True)
````
And this results in a neat line chart of the BTC value over the last 11 months.

You'd prefer a bar chart? Easy. Just substitute ``mark_line()`` with ``mark_bar()``.

Here are the two charts.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/altair-btc-line-bar.png)

This works well for charting a single column but if we wanted to have both BTC and ETH on the same graph, we need to manipulate the data a little - well quite a lot, really.

In terms of the crypto chart, we need to put both BTC and ETH values in the same column. But as we need to distinguish between them, we need another column that labels them _BTC_ or _ETH_.

Similarly, with the sales data, each value must be in the same column and this time we need a new column that labels the values as _Widget_, _Wodget_ or _Wudget_.

We can transform our current dataframes with the Pandas ``melt()`` method. Here is the code:

```` Python
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
````
Now we have two new dataframes that look like this:

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/crypto1-sales1.png)

Same data, different format.

Which means we can do this:

```` Python
c = alt.Chart(cryptodf1).mark_line().encode(
    x='Month', 
    y='value', 
    color = 'Name:N'
    )

st.altair_chart(c)
````
The y-axis is now mapped onto the _value_ column which contains thevalues for both BTC and ETH. But now we have a third encoding ``color`` which is mapped onto the _Name_ column. So we have two lines of different colours on the same chart.

![](https://github.com/alanjones2/streamlitfromscratch/raw/main/images/altair-line-btc-eth.png)

### Bokeh

### Conclusion