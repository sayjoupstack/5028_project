from flask import Flask
from tasks import add

app = Flask(__name__)

@app.route('/')
def index():
    return add.delay(1, 2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)