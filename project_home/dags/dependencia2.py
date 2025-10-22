from airflow.sdk import dag, task


@task()
def inicio() -> None:
    print('iniciando')


@task()
def segunda_tarefa(resultado_anterior: None) -> None:
    print('segunda tarefa')


@task()
def terceira_tarefa(resultado_anterior: None) -> None:
    print('terceira tarefa')


@task()
def final(resultado_anterior: None) -> None:
    print('final')


@dag()
def dependencia2():
    resultado_inicio = inicio()
    resultado_segunda = segunda_tarefa(resultado_inicio)
    resultado_terceira = terceira_tarefa(resultado_segunda)
    final(resultado_terceira)


# dependencia2()
