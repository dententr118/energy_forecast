from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.api_client import get_history, get_power_breakdown
from src.data_cleaner import clean_and_save


with DAG(
    dag_id="carbon_intensity_pipline",
    start_date=datetime.now(),
    schedule="@daily",
    catchup=False
) as dag:

    fetch_data_task = PythonOperator(
        task_id="fetch_raw_data",
        python_callable=get_history
    )

    clean_data_task = PythonOperator(
        task_id="process_data",
        python_callable=clean_and_save
    )

    fetch_data_task >> clean_data_task