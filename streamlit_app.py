import matplotlib.pyplot as plt
import streamlit as st
from collections import namedtuple
import math
import pandas as pd
import numpy as np
import plost                # this package is used to create plots/charts within streamlit
import seaborn as sns
from PIL import Image       # this package is used to put images within streamlit
from api_connection import get_data_from_api       # keep this commented if not using it otherwise brakes the app
from api_connection2 import get_data_api

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# API DATA N.1. FORECAST TEMPERATURE AND WEATHER REQUEST

outputs = get_data_from_api()
temperature = []
wind_speed = []
daysrange = range(len(outputs))
for ii in daysrange:
    for jj in range(len(outputs[ii]['hour'])):
        time = outputs[ii]['hour'][jj]['time']
        temp = outputs[ii]['hour'][jj]['temp_c']
        ws_mph = outputs[ii]['hour'][jj]['wind_mph']*0.44704
        temperature.append([temp])
        wind_speed.append([ws_mph])
 
## PLOT OF FORECASRTED TEMPERATURE AND WEATHER

plt.style.use('ggplot')   
fig,ax = plt.subplots(figsize=(10,6)) #It gives the size of the figure 
ax.plot(temperature, marker='.', linewidth=0.9, color='red',label='Temperature') # plot first the x, then the y and then the plot
ax.set_ylabel('Temperature [ºC]', color='red')
ax2=ax.twinx()
ax2.plot(wind_speed, marker='.', linewidth=0.9, color= 'purple',label='Wind speed') # plot first the x, then the y and then the plot
ax2.set_ylabel('Wind speed [m/s]', color='purple')
plt.title('Temperature and wind speed 3 days forecast in Barcelona') 
plt.xlabel('Hour')
plt.savefig('./Temp_vs_windspeed.png', dpi=300) #It saves it in this folder 

## API DATA N.2. CURRENT WEATHER DATA REQUEST

outputs2 = get_data_api()

## WEB APP DESIGN
# Row A
a1, a2 = st.columns(2)
a1.image(Image.open('upc_logo.png'))
a1.text("This website gets data from two different APIs. On one hand we have\nthe temperature and wind speed forecast data for 3 days, which is\nshown in the plot. On the other hand, real time temperature, wind\nspeed, humidity percentage and the outside feeling temperature are\nshown below.This website has been made to keep the user updated of\nthe weather in order to know if they should wear a coat or not.\n¡¡Thanks for visiting!!")
a2.image(Image.open('Temp_vs_windspeed.png'))

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature [°C]", outputs2['temp_c'])
b2.metric("Wind [m/s]", outputs2['wind_mph']*0.44704)
b3.metric("Humidity [%]",outputs2['humidity'])
b4.metric("How it feels outside? [°C]",outputs2['feelslike_c'])

