from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "Version 1")

@app.route("/")
def home():
    return f"Hello from {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)