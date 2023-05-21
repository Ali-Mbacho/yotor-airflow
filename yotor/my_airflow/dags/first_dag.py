from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'sparta',
    'retries': 5, 
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id ="first_dag",
    description = "This is first airflow dag",
    start_date = datetime(2023, 5, 7, 1),
    schedule_interval ='@daily',
    default_args = default_args
) as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command="echo hello world, this is first task"
    )

    task1