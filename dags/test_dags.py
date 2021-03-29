import datetime as dt
from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


default_args = {
    'start_date': dt.datetime.now() - dt.timedelta(days=7),
    'owner': 'airflow'
}

with DAG(dag_id='test_dag_success', description='A DAG that should never fail', default_args=default_args, tags=['test'], schedule_interval=None) as dag:

    dummy_task = DummyOperator(
        task_id='dummy_task'
    )

    dummy_task2 = DummyOperator(
        task_id='dummy_task2'
    )

    dummy_task >> dummy_task2


def throw_error():
    raise Exception('It failed!')


with DAG(dag_id='test_dag_failure', description='A DAG that always fail.', default_args=default_args, tags=['test'], schedule_interval=None) as dag:

    should_succeed = DummyOperator(
        task_id='should_succeed'
    )

    should_fail = PythonOperator(
        task_id='should_fail',
        python_callable=throw_error
    )

    should_succeed >> should_fail
