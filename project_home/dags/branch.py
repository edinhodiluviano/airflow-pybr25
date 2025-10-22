from airflow.sdk import dag, task


@task.branch
def branch_task():
    return 'odd_task' if random.randint(1, 2) == 1 else 'even_task'


@task
def odd_task():
    return


@task
def even_task():
    return



@dag()
def branch():
    branch_task() >> [odd_task(), even_task()]


# branch()
