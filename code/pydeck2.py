
#######################################
# !!!! THIS IS NOT WORKING CODE !!!!! #
#######################################

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

#CATTLE_DATA = "https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/nm_cattle.csv"
#POULTRY_DATA = "https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/nm_chickens.csv"


#HEADER = ["lng", "lat", "weight"]
#cattle_df = pd.read_csv(CATTLE_DATA, header=None).sample(frac=0.5)
#poultry_df = pd.read_csv(POULTRY_DATA, header=None).sample(frac=0.5)

#cattle_df.columns = HEADER


#cattle_df

w_df = pd.read_csv('https://github.com/alanjones2/uk-historical-weather/raw/main/data/stations.csv')
w_df['Name'] = w_df['Name'].str.replace(' ','_')

for n in w_df["Name"]:
    s = pd.read_csv(f'https://github.com/alanjones2/uk-historical-weather/raw/main/data/{n}.csv')
    
    tmp = s[(s['Year']==2019)]
    tmp = tmp[tmp['Month']==6]
    w_df[w_df["Name"] == s]['max'] = tmp

w_df
view = pdk.data_utils.compute_view(w_df[["lon", "lat"]])
view.zoom = 5

"""
cattle = pdk.Layer(
    "HeatmapLayer",
    data=cattle_df,
    opacity=0.9,
    get_position=["lng", "lat"],
    aggregation=pdk.types.String("MEAN"),
    threshold=1,
    get_weight="weight",
    pickable=True,
)
"""
stations = pdk.Layer(
    "HeatmapLayer",
    data=w_df,
    #opacity=1,
    get_position=["lon", "lat"],
    #threshold=0.5,
    get_weight="opened",
    #pickable=True,
    intensity=0.5
)

r = pdk.Deck(
    layers=[stations],
    initial_view_state=view,
    #map_provider="mapbox",
    map_style=pdk.map_styles.CARTO_LIGHT,#     .SATELLITE,
)

st.pydeck_chart(r)