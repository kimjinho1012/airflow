from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id='dags_bash_sensor',
    start_date=pendulum.datetime(2024,1,18, tz='Asia/Seoul'),
    schedule='0 0 * * *',
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo whoami'
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo $HOSTNAME'
    )

    bash_t1 >> bash_t2