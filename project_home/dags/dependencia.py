from airflow.sdk import dag, task


@task()
def inicio() -> None:
    print('iniciando')


@task()
def segunda_tarefa() -> None:
    print('segunda tarefa')


@task()
def terceira_tarefa() -> None:
    print('terceira tarefa')


@task()
def final() -> None:
    print('final')


@dag()
def dependencia():
    inicio() >> segunda_tarefa() >> terceira_tarefa() >> final()


# dependencia()
