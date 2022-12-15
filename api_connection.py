""" This script store the function required to stream data from the API of your choice"""

import requests
import json
import pandas as pd
import numpy as np

# create GET request

def get_data_from_api():
    
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    header = {"X-RapidAPI-Key": "6a425b2a7bmshc1f059e65b98fb7p1cdd78jsn184965114ca2",
               "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"}
    params = {"q":"Barcelona","days":"7"}

    response = requests.get(url, headers=header, params=params)
    outputs = response.json()['forecast']['forecastday']
    return outputs