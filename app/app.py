"""import os for env variables"""
import os
from flask import Flask


app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "Version 2")


@app.route("/")
def home():
    """
    home page
    """
    return f"Hello from {VERSION}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
