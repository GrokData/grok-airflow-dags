import datetime as dt
from airflow.models import DAG
from airflow.operators.dummy import DummyOperator


default_args = {
    'start_date': dt.datetime.now() - dt.timedelta(days=7),
    'owner': 'airflow'
}

with DAG(dag_id='test_dag', default_args=default_args, tags=['test'], schedule_interval=None) as dag:

    dummy_task = DummyOperator(
        task_id='dummy_task'
    )

    dummy_task2 = DummyOperator(
        task_id='dummy_task2'
    )

    dummy_task >> dummy_task2
