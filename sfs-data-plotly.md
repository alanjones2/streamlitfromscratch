# Plotly

Plotly is one of the most popular plotting packages for Python and the web. It is arguably easier to use than Altair and better looking than Pyplot — although there are some restrictions on its use in Streamlit.

We will use the package recommended by Plotly, Plotly Express, and to use it we import it like this.

```` Python
import plotly.express as px
````

Here is the simple line chart that we have seen before plotting the values of ETH and BTC plotted with Plotly Express.

<img src="./images/plotly-line-crypto.png" width="50%">

The code is pretty simple. Using px.line() to draw a line graph, we specify the data, the x- and y-axes and a data column to use to colour the lines that we plot.

```` Python
c = px.line(cryptodf1, x="Month", y="value",
             color='Name', 
             height=400)

st.plotly_chart(c)
````

I have additionally set the height of the figure.

Bar charts are as easy. Here is a grouped bar chart of our sales data.

<img src="./images/plotly-grouped-bar-crypto.png" width="50%">

And this is the code.

```` Python
c = px.bar(salesdf1, x="Quarter", y="value",
             color='Name', barmode='group',
             height=400)

st.plotly_chart(c)
````

We are employing ``px.bar()`` to draw the chart but apart from that the only difference between this and the line chart is that can you specify the barmode which is either group or stack.

Plotly is one of the simplest packages to get started with but I have a slight problem with the default colour scheme, I don’t really like it that much - I admit this is a purely personal gripe.

__Note: Streamlit have now changed the default theme for Plotly and it is now much more in keeping with the rest of Streamlit - a big improvement. This part of the tutorial will be updated to reflect the change.__

Plotly charts are interactive. Hovering over them shows you the data points and you can also pan and zoom in on a plot.
