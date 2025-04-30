from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv("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")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    return jsonify(response.json())

@app.route("/")
def home():
    return "Proxy server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
