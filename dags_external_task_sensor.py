from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
import pendulum
from datetime import timedelta
from airflow.utils.state import State
from airflow.models import Variable

email_str = Variable.get("email_target")
email_list = [email.strip() for email in email_str.split(",")]

with DAG(
    dag_id='dags_external_task_sensor',
    start_date=pendulum.datetime(2024, 1, 15, tz="Asia/Seoul"),
    schedule='0 7 * * *',
    catchup=False
) as dag:
    
    external_task_sensor_a = ExternalTaskSensor(
        task_id = 'external_task_sensor_a',
        external_dag_id="dags_branch_python_operator",

    )