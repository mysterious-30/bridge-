from flask import Flask, jsonify, request
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.remote_addr or "unknown"
    print(f"👋 Visitor IP: {ip}")
    return f"Welcome! Your IP is {ip}"

@app.route("/signal")
def signal():
    sig = random.choice(["BUY", "SELL", "WAIT"])
    print(f"📡 Signal sent: {sig}")
    return jsonify(signal=sig)

@app.route("/log", methods=["POST"])
def log_alert():
    data = request.get_json(force=True) or {}
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"📩 [{timestamp}] Received alert: {data}")
    return jsonify(status="success", received=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
