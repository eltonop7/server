from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = "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"

@app.route('/chat', methods=['POST'])
def proxy_chat():
    data = request.get_json()
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "ProxyBridge"
    }
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=20
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

