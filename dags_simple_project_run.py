from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException

with DAG(
    dag_id="dags_simple_project_run",
    start_date=pendulum.datetime(2024, 1, 8, tz="Asia/Seoul"),
    schedule="30 9 * * *",
    catchup=False
) as dag:
    
    @task(task_id="start_task")
    def comment():
        print("시작합니다........")

   
    job_run = BashOperator(
        task_id="job_run",
        bash_command="java -jar /opt/airflow/plugins/simple_project.jar "
    )

    comment() >> job_run