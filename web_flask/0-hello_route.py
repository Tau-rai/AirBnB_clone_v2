#!/usr/bin/python3
"""
This file ccontains a script that starts a Flask web applications
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays a string"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
