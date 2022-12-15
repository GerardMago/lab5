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

# API DATA N.1. FORECAST

seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
# replace the previous data with your own streamed data from API
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
 
## PLOT 1
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

## API DATA N.2
outputs2 = get_data_api()
### Here starts the web app design
# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('upc_logo.png'))
a2.image(Image.open('Temp_vs_windspeed.png'))
a3.text("This website it's provisional and has been made\nto keep the user updated of the weather in real\ntime. Thanks for visiting!")
#a3.metric("Actual Date", outputs2['localtime'])
#a3.metric("Humidity", "86%", "4%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature [°C]", outputs2['temp_c'])
b2.metric("Wind [m/s]", outputs2['wind_mph']*0.44704)
b3.metric("Humidity [%]",outputs2['humidity'])
b4.metric("How it feels outside? [°C]",outputs2['feelslike_c'])

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')              # text is created with markdown
    plost.time_hist(                        # histogram
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.bar_chart(
    #plost.donut_chart(                      # donut charts
    data=stocks,
    bar='company',
    value=['q2', 'q3'],
    group='value',
    color='company',
    legend=None)  