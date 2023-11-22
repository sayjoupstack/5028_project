# encoding=utf8
from flask import Flask, render_template, flash, request
from dotenv import load_dotenv
from task import send_mail
import os
import smtplib
from email.mime.text import MIMEText
import requests
from db_method import CRUD

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASH_SECRET_KEY")

# TEST THIS METHOD
def getWeatherInfo():
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json?key="+api_key+"&q=seoul&aqi=no"
    return requests.get(url).json()

def test_getWeatherInfo():
    result = getWeatherInfo()
    assert result["location"]["name"] == "Seoul"

@app.route('/')
def index():
    response = getWeatherInfo()
    localtime = response["location"]["localtime"]
    temp_c = response["current"]["temp_c"]
    temp_f = response["current"]["temp_f"]
    condition_text = response["current"]["condition"]["text"]
    condition_icon = response["current"]["condition"]["icon"]
    
    return render_template('index.html', 
                           localtime=localtime, 
                           temp_c=temp_c, 
                           temp_f=temp_f, 
                           condition_text=condition_text, 
                           condition_icon=condition_icon)

@app.route("/mail",methods=['POST'])
def mail():
    content = request.form["content"]
    db = CRUD()
    db.insertDB(schema='public',table='mail',colum='content',data=content)
    flash(content)
    send_mail.delay(content)
    return render_template("send.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)