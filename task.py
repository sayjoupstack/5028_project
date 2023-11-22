from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

app = Celery('tasks', backend='rpc://', broker='pyamqp://'+os.getenv("RABBITMQ_USER")+':'+os.getenv("RABBITMQ_PASSWORD")+'@'+os.getenv("RABBITMQ_HOST")+'/')

@app.task
def add(x, y):
    return x + y