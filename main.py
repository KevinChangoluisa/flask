from flask import Flask, jsonify
import requests
import base64
from configparser import ConfigParser
import os


config = ConfigParser()
config.read('config.ini')
wrf_config = config['WRF']

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/get_imgWRF', methods=['POST'])
def get_imgWRF():
    url = request.json.get('url')
    username = wrf_config.get('USERNAME')
    password = wrf_config.get('PASSWORD')
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    base64_data = base64.b64encode(response.content).decode('utf-8')
    return base64_data


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
