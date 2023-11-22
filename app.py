from flask import Flask
from dotenv import load_dotenv
from task import add
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    # result = add.delay(1, 2)
    return "main"

@app.route("/mail",methods=['POST'])
def mail():          
    content = "test"
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)