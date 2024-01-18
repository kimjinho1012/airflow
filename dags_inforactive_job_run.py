from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException

with DAG(
    dag_id="dags_inforactive_job_run",
    start_date=pendulum.datetime(2024, 1, 8, tz="Asia/Seoul"),
    schedule="30 9 * * *",
    catchup=False
) as dag:
    
    @task(task_id="start_task")
    def comment():
        print("시작합니다........")

    @task(task_id="exists_file")
    def exists_file():
        import os
        if not os.path.exists("/opt/airflow/plugins/jobs/TEST/TEST_run.sh"):
            raise AirflowException("/opt/airflow/plugins/jobs/TEST/TEST_run.sh not founded!!!!") 
   
    job_run = BashOperator(
        task_id="job_run",
        bash_command="{{var.value.sh_path}} ",
        trigger_rule="all_success"
    )

    comment() >> exists_file() >>job_run