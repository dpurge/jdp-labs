from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    "welcome",
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
