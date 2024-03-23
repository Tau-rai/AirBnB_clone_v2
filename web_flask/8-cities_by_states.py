#!/usr/bin/python3
"""
This file contains a script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """Lists all the cities by state"""
    states = storage.all(State).values()
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(error):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
