from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id='dags_python_with_op_kwargs',
    start_date=pendulum.datetime(2026, 5, 1, tz='Asia/Seoul'),
    schedule='10 10 * * *',
    catchup=False
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id='regist2_t1',
        python_callable=regist2,
        op_args=['kimjinho', 'man', 'kr','seoul'],
        op_kwargs={'email':'kimjinho@naver.com', 'phone':'010'}
    )
    
    regist2_t1