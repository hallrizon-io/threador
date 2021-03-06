<html>
<h1>Parallel computing using Celery - <b>threador</b></h1>

<h2> Install library:</h2>
<pre>pip install threador</pre>


<h2>Step 1</h2>
<p>Init docker container with RabbitMQ</p>
<pre>docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management</pre>

<h2>Step 2</h2>
<p>Create fite `threador_config.py` in your root place at the project.</p>

<pre>
import time
from celery import Celery
from threador.tasks import Task

app = Celery('threador_celery', backend='rpc://', broker='pyamqp://guest@localhost//')

// Your task for parallel execution
class SleepTask(Task):
    def fnc(self, *args, **kwargs):
        _r = kwargs.get('timeout', 0)
        time.sleep(_r)
        return _r

// Register all your task here
tasks = {
    'sleep': SleepTask(),
}

// Required function for call your task parallel
@app.task
def call_task(fnc_name: str, *args, **kwargs):
    fnc = tasks.get(fnc_name, None)
    if fnc is not None:
        result = fnc(*args, **kwargs)
        return result
</pre>
<h2>Step 3</h2>
<p>Run celery for correct working.</p>
<pre>celery -A threador_config worker --loglevel=debug -n threador_celery@parallel</pre>

<h2>Step 4</h2>
<p>Using parallel computing in code.</p>
<p>Result will be order by position in tasks.</p>
<pre>
from threador.contrib import Executor
parallel = Executor(tasks=(
    ['sleep', None, {'timeout': 3}],
    ['sleep', None, {'timeout': 2}],
    ['sleep', None, {'timeout': 4}],
))
result = parallel.run()
print(result)
</pre>
</html>
