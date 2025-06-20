import streamlit as slt
import ee
import xarray as xr

# authenticate and initialize gee
ee.Authenticate()
ee.Initialize(project = "ee-subsonic", opt_url = 'https://earthengine-highvolume.googleapis.com')

# open image collection
data = ee.ImageCollection("ECMWF/ERA5_LAND/DAILY_AGGR").filterDate("2010","2025")\
.select(["temperature_2m"])

# convert to xarray dataset
data_ds = xr.open_dataset(data, engine = "ee")

# convert dataset value from degree kelvin to degree celcius
