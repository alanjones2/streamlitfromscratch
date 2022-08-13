
#######################################
# !!!! THIS IS NOT WORKING CODE !!!!! #
#######################################

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

year = st.slider("Select Year", 1950,2020,2020)
    
st.subheader(year)
w_df = pd.read_csv('https://github.com/alanjones2/uk-historical-weather/raw/main/data/stations.csv')
w_df['Name'] = w_df['Name'].str.replace(' ','_')
w_df['max'] = None

#colorRange = [[140,81,10],[216,179,101],[246,232,195],[199,234,229],[90,180,172],[1,102,94]]

for n in w_df["Name"]:
    s = pd.read_csv(f'https://github.com/alanjones2/uk-historical-weather/raw/main/data/{n}.csv')
    
    tmp = s[(s['Year']==year)]
    tmp = tmp[tmp['Month']==6]
    
    tmaxcol = tmp['Tmax'].values
    if len(tmaxcol) > 0:
        #f"name = {n} max = {tmp['Tmax'].values[0]}"
        ix = w_df.index[[w_df["Name"] == n]]
        w_df.iloc[ix,4] = tmp['Tmax'].values[0]
        #w_df[w_df["Name"] == n]
    
#st.dataframe(w_df)

view = pdk.data_utils.compute_view(w_df[["lon", "lat"]])
view.zoom = 4.5

stations = pdk.Layer(
    "HeatmapLayer",
    data=w_df,
    opacity=0.1,
    get_position=["lon", "lat"],
    #aggregation=pdk.types.String("SUM"),
    #threshold=0.5,
    #colorRange = colorRange,
    get_weight="max",
    radiusPixels = 300,
    #threshold = 0,
    #pickable=True,
    #intensity=0.5
)

r = pdk.Deck(
    layers=[stations],
    initial_view_state=view,
    #map_provider="mapbox",
    map_style=pdk.map_styles.CARTO_LIGHT#     .SATELLITE,
)

st.pydeck_chart(r)