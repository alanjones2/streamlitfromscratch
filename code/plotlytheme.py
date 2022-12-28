import streamlit as st
import pandas as pd

import plotly.express as px

st.set_page_config(layout = "wide")

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

# st.info("### To compare more than one value, it's often easier to transform the data")
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

### Plotly

import plotly.express as px

st.info("## Plotly charts - new theme v old theme")

col1, col2 = st.columns(2)

col1.subheader('New theme')
col2.subheader('Old theme')

c = px.line(cryptodf1, x="Month", y="value",
             color='Name', 
             height=400)

col1.plotly_chart(c)

c = px.line(cryptodf1, x="Month", y="value",
             color='Name', 
             height=400)

col2.plotly_chart(c, theme=None)

c = px.bar(cryptodf1, x="Month", y="value",
             color='Name', barmode='group',
             height=400)

col1.plotly_chart(c)

c = px.bar(cryptodf1, x="Month", y="value",
             color='Name', barmode='group',
             height=400)

col2.plotly_chart(c, theme=None)

c = px.bar(salesdf1, x="Quarter", y="value",
             color='Name', barmode='group',
             height=400)

col1.plotly_chart(c)

c = px.bar(salesdf1, x="Quarter", y="value",
             color='Name', barmode='group',
             height=400)
col2.plotly_chart(c, theme=None)

c = px.bar(salesdf1, x="Quarter", y="value",
             color='Name', barmode='stack',
             height=400)
col1.plotly_chart(c)

c = px.bar(salesdf1, x="Quarter", y="value",
             color='Name', barmode='stack',
             height=400)
c.update_layout(paper_bgcolor="white", 
                plot_bgcolor="white", 
                yaxis_gridcolor= "black",
                yaxis_linecolor= "black",
                xaxis_linecolor= "black")
col2.plotly_chart(c, theme=None)
