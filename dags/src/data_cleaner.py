import pandas as pd
import os


RAW_PATH = "/opt/airflow/data/raw/raw_history.csv"
PROCESSED_PATH = "/opt/airflow/data/processed/processed_history.csv"

def clean_and_save():
    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError("Raw data file not found: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)
    df.drop(['updatedAt','createdAt','emissionFactorType','isEstimated','estimationMethod'], axis=1, inplace=True)
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print("Data cleaned and saved")