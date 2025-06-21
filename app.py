from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "online"})

@app.route('/status')
def status():
    return jsonify({"triggered": True})

if __name__ == '__main__':
    app.run()
