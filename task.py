from celery import Celery
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Celery('tasks', backend='rpc://', broker='pyamqp://'+os.getenv("RABBITMQ_USER")+':'+os.getenv("RABBITMQ_PASSWORD")+'@'+os.getenv("RABBITMQ_HOST")+'/')

@app.task
def add(x, y):
    return x + y

@app.task
def send_mail(content):
    content = content
    title = 'test'

    sender = os.getenv("MAIL_ADDRESS")
    receiver = os.getenv("MAIL_ADDRESS")
    app_password = os.getenv("APP_PASSWORD")

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, app_password)
    msg = MIMEText(content)
    msg['Subject'] = title
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    return "MAIL"