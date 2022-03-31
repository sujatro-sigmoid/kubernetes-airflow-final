from airflow.operators.postgres_operator import PostgresHook
import logging

def display_info():

    request = 'SELECT * FROM docker_dag_table;'
    pg_hook = PostgresHook(postgres_conn_id="postgres-service-db",
                           schema="airflow")
    cursor = pg_hook.get_conn().cursor()
    logging.info("Fetching data...")
    cursor.execute(request)
    rows = cursor.fetchall()
    for row in rows:
        logging.info(row)
    logging.info("Data fetched successfully!")
