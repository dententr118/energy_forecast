import os
from dotenv import load_dotenv

load_dotenv()
# Загружаю переменные окружения из .env файла

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.electricitymaps.com/v3/"
# URL от Electricity Maps API

RAW_DATA = "data/raw"
PROCESSED_DATA = "data/processed"
# Папки с сырыми и обработанными данными
