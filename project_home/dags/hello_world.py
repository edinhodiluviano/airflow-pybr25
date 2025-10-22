from airflow.sdk import dag, task


@task()
def hello_world_task() -> None:
    print('=' * 100)
    print('hello world')
    print('=' * 100)


@dag()
def hello_world_dag():
    hello_world_task()


hello_world_dag()
