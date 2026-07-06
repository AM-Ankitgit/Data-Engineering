import datetime

try:
    from airflow.providers.standard.operators.empty import EmptyOperator
    from airflow.providers.standard.operators.python import PythonOperator
    
    from airflow.providers.standard.operators.bash import BashOperator
except ImportError:
    from airflow.operators.empty import EmptyOperator
    from airflow.providers.bash import BashOperator
    from airflow.operators.python import PythonOperator

from airflow import DAG



def hello_world():
    print("Hello World!")

def bash_hello_world():
    return "bash_Hello World!"

default_args = {
    "owner": "airflow", 
    "start_date": datetime.datetime(2023, 1, 1),
    "retries": 1,
}


dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule="*/5 * * * *",
    max_active_runs=1,
)
bash_task = BashOperator(dag=dag, task_id="bash_task", bash_command="echo 'bash_Hello World!'")
python_task = PythonOperator(dag=dag, task_id="hello_world", python_callable=hello_world)
