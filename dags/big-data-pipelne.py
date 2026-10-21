from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests 
import os

from process_data import process_weather_data

#define args 
defult_args = {
    'owner': 'jason',
    'depend_on_past': False,
    'email_on_failure': False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)
}

#define Dag where it runs daly 
with DAG(
    dag_id='big_data_weather_pipeline',
    default_args=default_args,
    description='A scalable ETL pipeline using PySpark',
    schedule_interval=timedelta(days=1), # Runs daily
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['pyspark', 'etl', 'beginner']
    ) as dag:
    #extract the data set 
    def download_sample_data():
        print("downloading the dataset ")

    data_dir = "/opt/airflow/data"
    os.makedirs(data_dir, exist_ok=True)
        
    csv_content = """City,Temp_Celsius,Humidity,Recorded_At
Nairobi,22.5,65,2023-10-01
Nairobi,23.1,60,2023-10-02
London,15.0,80,2023-10-01
London,14.5,82,2023-10-02
Tokyo,28.0,70,2023-10-01
Tokyo,29.5,68,2023-10-02
Nairobi,21.0,75,2023-10-03
London,16.2,78,2023-10-03"""
        
    with open(f"{data_dir}/raw_weather.csv", "w") as f:
            f.write(csv_content)
    print("✅ Data downloaded successfully!")

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=download_sample_data,
    )

    transform_load_task = PythonOperator(
        task_id = 'transform and load',
        python_callable = process_weather_data
    )

    #define order of tasks pf the pipeline 
    extract_task >> transform_load_task