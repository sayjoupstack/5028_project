from flask import Flask
from task import add

app = Flask(__name__)

@app.route('/')
def index():
    result = add.delay(1, 2)
    return result.get()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)