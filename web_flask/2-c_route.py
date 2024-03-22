#!/usr/bin/python3
"""
This file contains a script that starts a Flask web application,
that listens on 0.0.0.0 port 5000
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays a string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays C folowed by some text"""
    return f"C { text.replace('_', ' ') }"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
