from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import datetime
from common.common_func import get_sftp

with DAG(
    dag_id='dags_python_import.py',
    start_date=pendulum.datetime(2024,1,18, tz='Asia/Seoul'),
    schedule='30 6 * * *',
    catchup=False
) as dag:

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=get_sftp
    )

    py_t1