import requests
from src.config import BASE_URL, ZONE, API_KEY
import pandas as pd
import os

HEADERS = {"auth-token": API_KEY} if API_KEY else {}

RAW_PATH = "/opt/airflow/data/raw/raw_history.csv"

def get_history(zone=ZONE):
    url = f"{BASE_URL}/carbon-intensity/history"
    params = {"zone": zone}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    # Создаём папку если её нет
    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)

    # Преобразуем JSON в DataFrame
    history = pd.json_normalize(response.json()["history"])

    # Сохраняем в CSV
    history.to_csv(RAW_PATH, index=False)

    return history

def get_power_breakdown(zone=ZONE):
    url = f"{BASE_URL}/power-breakdown/history"
    params = {"zone": zone}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

