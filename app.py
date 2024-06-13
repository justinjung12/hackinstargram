from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

saved_data = []

@app.route('/', methods=['POST'])
def save():
    saved_dataip = request.get_json()['ip']   
    saved_datatime = request.get_json()['date']
    saved_data.append({'ip':saved_dataip,'time':saved_datatime})
    return 'ok'

@app.route('/wjadmin')
def admin():
    return saved_data
@app.route('/deleteallip')
def deleteallip():
    saved_data = []
    return 'del'
