""" This script store the function required to stream data from the API of your choice"""

import requests
import json
import pandas as pd
import numpy as np

# create GET request

def get_data_api():
    
    url = 'https://weatherapi-com.p.rapidapi.com/current.json'
    header = {'X-RapidAPI-Key': 'ca6cdeb39amsh740cd5fc7aa6b08p15f055jsndcca0ef04eb8',
               'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'}
    params = {'q':'Barcelona'}

    response = requests.request("GET", url, headers=header, params=params)
    outputs2 = response.json()['current']
    return outputs2