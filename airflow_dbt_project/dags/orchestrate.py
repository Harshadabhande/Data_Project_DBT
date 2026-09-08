from datetime import timedelta
from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator



with DAG(
    dag_id="orchestrate",
    # schedule=None,
    schedule = "0 11 * * *",  # Run daily at midnight
    start_date=pendulum.datetime(year=2026,month=9,day=9,tz="Asia/Kolkata"),
    catchup=False,
) as dag:

    # 1. Databricks Job Triggering (Hardcoded parameters)
    # ingest_cdc = DatabricksRunNowOperator(
    #     task_id="ingest_cdc",
    #     databricks_conn_id='databricks_default',  # Bypass Airflow Connection lookup
    #     databricks_retry_args={
    #         "token":"dapif6237ba5576dff3e6d00539f1a7b7edf",  # Replace with your Databricks PAT
    #         "host": "https://dbc-c934318a-b975.cloud.databricks.com",  # Replace with your Databricks Host URL
    #     },
    #     job_id=756912004193826,
    #     execution_timeout=timedelta(seconds=3600),
    # )
    ingest_cdc = DatabricksRunNowOperator(
        task_id="ingest_cdc",
        databricks_conn_id="databricks_default",
        job_id=756912004193826,
        execution_timeout=timedelta(seconds=3600),
    )
    # 2. Bash Tasks
    @task.bash
    def clean_target() -> str:
        return "rm -rf /opt/airflow/walmart_project/target && rm -rf /opt/airflow/walmart_project/logs"

    @task.bash
    def source_freshness() -> str:
        return "cd /opt/airflow/walmart_project && dbt source freshness"

    @task.bash
    def silver_technical() -> str:
        return "cd /opt/airflow/walmart_project && dbt run --select silver_t"

    @task.bash
    def silver_technical_tests() -> str:
        return "cd /opt/airflow/walmart_project && dbt test --select silver_t"

    @task.bash
    def silver_business() -> str:
        return "cd /opt/airflow/walmart_project && dbt run --select silver_b"

    @task.bash
    def silver_business_tests() -> str:
        return "cd /opt/airflow/walmart_project && dbt test --select silver_b"

    @task.bash
    def gold_ephemeral() -> str:
        return "cd /opt/airflow/walmart_project && dbt run --select gold/ephemeral"

    @task.bash
    def gold_dimensions() -> str:
        return "cd /opt/airflow/walmart_project && dbt snapshot"

    @task.bash
    def gold_facts() -> str:
        return "cd /opt/airflow/walmart_project && dbt run --select gold/facts"

    # 3. Pipeline Dependencies
    (
        ingest_cdc
        >> clean_target()
        >> source_freshness()
        >> silver_technical()
        >> silver_technical_tests()
        >> silver_business()
        >> silver_business_tests()
        >> gold_ephemeral()
        >> gold_dimensions()
        >> gold_facts()
    )