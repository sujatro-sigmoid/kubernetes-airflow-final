# kubernetes-airflow-final

Kubernetes Task
- Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
- Deploy airflow and postgres
- Schedule the dag
- Validate entry in postgres

Steps to run:
- Terminal 1:
  - minikube start
  - minikube mount ./dags/:/mnt/airflow/dags
- Terminal 2:
  - ./script-create.sh (do chmod +x ./script-create.sh if required)
  - kubectl get pod
  - kubectl exec -it puckel-deploy-pod-name bash
  - FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
  - export FERNET_KEY=$FERNET_KEY
  - airflow initdb
  - exit
  - kubectl port-forward svc/puckel-service 8080:8080
- Open localhost:8080 and create a postgres connection and run the dag.
  - (postgres_conn_id="postgres-service-db",host="postgres-service-db",schema="airflow", user="airflow", password="airflow", port='5432')
- Terminal 3: To verify: 
  - kubectl exec -it postgres-deploy-pod-name bash
  - psql -U airflow
  - SELECT * FROM table_name;
