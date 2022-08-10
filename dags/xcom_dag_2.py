from sched import scheduler
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime


def _t1():
    None


def _t2():
    None


def _t3():
    None


with DAG('xcom_dag_2', start_date+datetime(2022, 1, 1), schedule_interval='@daily', catchup=False) as dag:

    t1 = PythonOperator(
        task_id='t1',
        pthone_callable=_t1
    )

    t2 = PythonOperator(
        task_id='t2',
        pthone_callable=_t2
    )

    t3 = PythonOperator(
        task_id='t3',
        pthone_callable=_t3
    )

t1 >> t2 >> t3
