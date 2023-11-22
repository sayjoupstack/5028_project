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

    msg = MIMEText(content)
    msg['Subject'] = title

    # (*)메일의 발신자 메일 주소, 수신자 메일 주소, 앱비밀번호(발신자) 
    sender = os.getenv("MAIL_ADDRESS")
    receiver = os.getenv("MAIL_ADDRESS")
    app_password = os.getenv("APP_PASSWORD")


    # 세션 생성
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(sender, app_password)
        s.sendmail(sender, receiver, msg.as_string())    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)