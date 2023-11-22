from celery import Celery

app = Celery('tasks', broker='pyamqp://admin:whtpehd6298!@localhost:15672/')

@app.task
def add(x, y):
    return x + y