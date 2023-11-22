from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://admin:whtpehd6298!@localhost:5672/')

@app.task
def add(x, y):
    return x + y