from datetime import datetime

from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG

with DAG(
    "ek1_dag", start_date=datetime(2017, 3, 20),
    schedule_interval="@daily", catchup=False
) as dag:
    op = DummyOperator(task_id="ek1_task")
