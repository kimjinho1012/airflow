from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_inforactive_job_run",
    start_date=pendulum.datetime(2024, 1, 25, tz="Asia/Seoul"),
    schedule="30 11 * * *",
    catchup=False
) as dag:
    file_path = '/CDS_TEST/CDS_TEST_run.sh '

    job_run = BashOperator(
        task_id="job_run",
        bash_command="{{var.value.job_root_path}}" + file_path + ' &&'
        'echo SUCCESS'
    )

    @task.branch(task_id="job_run_result_branch")
    def job_run_result_branch(**kwargs):
        ti = kwargs["ti"]
        result = ti.xcom_pull(key="return_value", task_ids ="job_run")
        if result == 'SUCCESS':
            return "send_success_email_task"
        else:
            return "send_fail_email_task"




    send_success_email_task = EmailOperator(
        task_id = 'send_success_email_task',
        to='kjhkjh900@naver.com',
        subject='Airflow 성공메일',
        html_content='dags_inforactive_job_run 작업 성공입니다.',
    )

    send_fail_email_task = EmailOperator(
        task_id = 'send_fail_email_task',
        to='kjhkjh900@naver.com',
        subject='Airflow 실패메일',
        html_content='dags_inforactive_job_run 작업 실패입니다.',
    )

    job_run >> job_run_result_branch() >> [send_success_email_task, send_fail_email_task]