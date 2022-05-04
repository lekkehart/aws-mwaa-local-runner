from datetime import datetime

from airflow.decorators import dag, task


@task.virtualenv(requirements=[
    "art"
])
def draw():
    from art import aprint

    for _ in range(10):
        aprint("random")


@dag(
    dag_id="ex_virtualenv",
    description="Installs 'art' in a virtual environment and prints 10 random ascii art texts",
    schedule_interval=None,
    start_date=datetime(2017, 3, 20),
    catchup=False
)
def drawer():
    draw()


d = drawer()
