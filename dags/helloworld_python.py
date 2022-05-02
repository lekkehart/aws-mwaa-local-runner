from datetime import datetime

import airflow.operators.python
from airflow import DAG


def print_hello():
    return 'Hello world from first Airflow DAG!'


dag = DAG('helloworld_python', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = airflow.operators.python.PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
hello_operator_2 = airflow.operators.python.PythonOperator(task_id='hello_task2', python_callable=print_hello, dag=dag)


hello_operator >> hello_operator_2

