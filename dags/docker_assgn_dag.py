from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from python_scripts.display_table_info import display_info

with DAG(
        dag_id="docker_assgn_dag",
        default_args={
            "retries": 1,
            "retry_delay": timedelta(seconds=30),
        },
        start_date=datetime(year=2022, month=3, day=30),
        schedule_interval="@once",
        catchup=False
) as dag:
    task_insert = PostgresOperator(
        task_id="insert_time_of_dag_execution",
        postgres_conn_id="postgres-service-db",
        sql="sql/create_insert_table.sql"
    )

    task_display = PythonOperator(
        task_id="display_table",
        python_callable=display_info
        )

    task_insert >> task_display

