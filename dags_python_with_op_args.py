from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id='dags_python_with_op_args',
    start_date=pendulum.datetime(2024,1,18, tz='Asia/Seoul'),
    schedule='30 6 * * *',
    catchup=False
) as dag:
    regist_1 = PythonOperator(
        task_id='regist_1',
        python_callable=regist,
        op_args=['kimjinho', 'man', 'kr', 'seoul']
    )

    regist_1
