from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.decorators import BashOperator

with DAG(
    dag_id="dags_bash_python_with_xcom",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 1, 8, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id="python_push")
    def python_push_xcom():
        result_dic = {"status":"good", "data":[1,2,3], "options_cnt":100}
        return result_dic
    
    bash_pull = BashOperator(
        task_id="bash_pull",
        env={"STATUS":"{{ti.xcom_pull(task_ids='python_push')['status']}}",
            "DATA":"{{ti.xcom_pull(task_ids='python_push')['data']}}",
            "OPTIONS_CNT":"{{ti.xcom_pull(task_ids='python_push')['options_cnt']}}"
            },
        bash_command="echo $STATUS && echo $DATA && echo $OPTIONS_CNT"
    )

    python_push_xcom() >> bash_pull