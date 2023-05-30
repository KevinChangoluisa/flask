from flask import Flask, jsonify ,request
import requests
import base64
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/get_imgWRF', methods=['POST'])
def get_imgWRF():
    url = request.json.get('url')
    print("La url es: ",url)
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    base64_data = base64.b64encode(response.content).decode('utf-8')
    return base64_data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
