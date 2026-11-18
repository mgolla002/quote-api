import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    "Make it work, make it right, make it fast.",
    "Simple is better than complex.",
    "Readability counts.",
]

@app.route("/")
def home():
    return "Quote API is running"

@app.route("/quote")
def quote():
    return jsonify(quote=random.choice(QUOTES))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)