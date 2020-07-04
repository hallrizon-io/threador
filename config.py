from celery import Celery

from threador.classes.Task import Task

import random
import time

# celery -A main worker --loglevel=debug
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
app = Celery('downloaderApp', backend='rpc://', broker='pyamqp://guest@localhost//')


class SleepTest(Task):
    def fnc(self, *args, **kwargs):
        _r = random.randint(0, 20)
        time.sleep(_r)
        return _r


class ComputeTask(Task):
    def fnc(self, *args, **kwargs):
        _r = kwargs.get('sleep', 0)
        time.sleep(_r)
        return _r


tasks = {
    'task': SleepTest(),
    'sleep': ComputeTask(),
}


@app.task
def call_task(fnc_name: str, *args, **kwargs):
    fnc = tasks.get(fnc_name, None)
    if fnc is not None:
        result = fnc(*args, **kwargs)
        return result
