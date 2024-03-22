#!/usr/bin/python3
"""
This file contains a script that starts a Flask web application,
that listens on 0.0.0.0 port 5000
"""


from flask import Flask, render_template


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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Displays Python folowed by some text"""
    return f"Python { text.replace('_', ' ') }"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays a number n id n is an integer"""
    return f"{ n } is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
