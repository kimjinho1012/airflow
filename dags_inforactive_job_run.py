from airflow import DAG
import pendulum
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
        bash_command="{{var.value.job_root_path}}" + file_path,
    )

    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to='kjhkjh900@naver.com',
        subject='Airflow 성공메일',
        html_content='Airflow 작업이 완료되었습니다.'
    )

    job_run >> send_email_task