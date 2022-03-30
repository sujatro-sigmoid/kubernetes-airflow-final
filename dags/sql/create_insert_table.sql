CREATE TABLE IF NOT EXISTS docker_dag_table (
sl_id SERIAL PRIMARY KEY,
iso_date_time VARCHAR UNIQUE NOT NULL);

INSERT INTO docker_dag_table(iso_date_time) VALUES('{{ ts }}');