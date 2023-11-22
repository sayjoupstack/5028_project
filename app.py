# encoding=utf8
from flask import Flask, render_template
from dotenv import load_dotenv
from task import send_mail
import os
import smtplib
from email.mime.text import MIMEText
import requests

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json?key="+api_key+"&q=seoul&aqi=no"
    response = requests.get(url).json()
    
    
    return render_template('index.html', localtime = response.location.localtime)

@app.route("/mail",methods=['POST'])
def mail():
    result = send_mail.delay()
    return "MAIL"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)