from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

MISSION_NAME = os.getenv("MISSION_NAME", "SPACE CONNECT")
APP_VERSION = os.getenv("APP_VERSION", "1.0")


@app.route("/")
def home():
    return jsonify({
        "mission": MISSION_NAME,
        "version": APP_VERSION,
        "status": "ONLINE",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/health")
def health():
    return jsonify({
        "service": "space-connect-app",
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)