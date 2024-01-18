from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import datetime

with DAG(
    dag_id='dags_python_operator',
    start_date=pendulum.datetime(2024,1,18, tz='Asia/Seoul'),
    schedule='30 6 * * *',
    catchup=False
) as dag:
    def select_fruit():
        fruit=['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        import random
        rand_it = random.randint(0, 3)
        print(fruit[rand_it])

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    py_t1