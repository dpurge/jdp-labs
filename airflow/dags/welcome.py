from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

with DAG(
    'welcome',
    default_args = default_args,
    description = 'Exaple pipeline that prints out "Hello, World!"',
    start_date = datetime(2023, 11, 30),
    schedule = '@daily',
    catchup = False):

    print_date = BashOperator(
        task_id = 'print-date',
        bash_command = 'date')
    
    say_hello = BashOperator(
        task_id = 'say-hello',
        bash_command = 'echo "Hello, World!"')
    
    print_date >> say_hello
