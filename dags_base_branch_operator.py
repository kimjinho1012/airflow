from typing import Iterable
from airflow import DAG
from airflow.utils.context import Context
import pendulum
from airflow.operators.branch import BaseBranchOperator
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_base_branch_operator",
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 8, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    class CustomBranchOperator(BaseBranchOperator):
        def choose_branch(self, context):
            import random
            print(context)
            item_list = ['A', 'B', 'C']
            selected_item = random.choice(item_list)
            if selected_item == 'A':
                return 'task_a'
            elif selected_item in ['B', 'C']:
                return ['task_b', 'task_c']