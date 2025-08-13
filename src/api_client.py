#import requests
#from config import API_KEY, BASE_URL
#
#try:
#    response = requests.get(
#        f"{BASE_URL}carbon-intensity/latest?zone=SE",
#        headers={
#            "auth-token": f"{API_KEY}"
#        }
#    )
#    response.raise_for_status()
#    print(response.json())
#except requests.exceptions.RequestException as e:
#    print(f"API request failed: {e}")
#
#
import requests
from config import BASE_URL, ZONE, API_KEY
import pandas as pd
from pandas import json_normalize

HEADERS = {"auth-token": API_KEY} if API_KEY else {}

def get_history(zone=ZONE):
    url = f"{BASE_URL}/carbon-intensity/history"
    params = {"zone": zone}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return json_normalize(response.json()['history'])

def get_power_breakdown(zone=ZONE):
    url = f"{BASE_URL}/power-breakdown/history"
    params = {"zone": zone}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

print(get_history())
pd.DataFrame(get_history()).to_csv("data/raw/history.csv", index=False)