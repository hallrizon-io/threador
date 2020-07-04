import time

from celery import Celery
from threador.tasks import Task

# celery -A threador_config worker --loglevel=debug -n threador_celery@parallel
app = Celery('threador_celery', backend='rpc://', broker='pyamqp://guest@localhost//', namespace='threador_celery')


# Your task for parallel execution
class SleepTask(Task):
    def fnc(self, *args, **kwargs):
        _r = kwargs.get('timeout', 0)
        time.sleep(_r)
        return _r


# Register all your task here
tasks = {
    'sleep': SleepTask(),
}


# Main function for call your tasks in code
@app.task
def call_task(fnc_name: str, *args, **kwargs):
    fnc = tasks.get(fnc_name, None)
    if fnc is not None:
        result = fnc(*args, **kwargs)
        return result
