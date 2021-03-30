import datetime as dt
from airflow.models import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'start_date': dt.datetime.now() - dt.timedelta(days=7),
    'owner': 'airflow'
}


def extract():
    print('Data extracted!')


def transform():
    print('Data transformed!')


def load():
    print('Data loaded!')


with DAG(dag_id='example_dag', description='An example ETL dag', default_args=default_args, tags=['test'], schedule_interval=None) as dag:

    extract_step = PythonOperator(
        task_id='extract',
        python_callable=extract
    )

    transform_step = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    load_step = PythonOperator(
        task_id='load',
        python_callable=load
    )

    extract >> transform >> load

