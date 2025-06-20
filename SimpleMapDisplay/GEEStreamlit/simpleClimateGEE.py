import streamlit as slt
import ee
import xarray as xr
import matplotlib.pyplot as plt

# authenticate and initialize gee
ee.Authenticate()
ee.Initialize(project = "ee-subsonic", opt_url = 'https://earthengine-highvolume.googleapis.com')

# open image collection
data = ee.ImageCollection("ECMWF/ERA5_LAND/DAILY_AGGR").filterDate("2010","2025")\
.select(["temperature_2m"])

# convert to xarray dataset
data_ds = xr.open_dataset(data, engine = "ee")

# convert dataset value from degree kelvin to degree celcius
cel_data = data_ds - 273.15

# calculate longterm average temperature and the temperature anomaly
yearly_mean = data_ds.resample(time = 'YE').mean('time')
longterm_mean = yearly_mean.resample.mean('time')
anomaly = yearly_mean - longterm_mean

# visualize longterm mean temperature
plt,ax = plt.subplots(figsize = (7,4))
longterm_mean["temperature_2m"].plot( x = 'lon', y = 'lat', ax = ax)
