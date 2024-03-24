#!/usr/bin/python3
"""
This file contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Lists all the states in the states list"""
    states = storage.all(State).values()
    return render_template("states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays a state and its cities if found"""
    state = None
    for obj in storage.all(State).values():
        if obj.id == id:
            state = obj
            break

    if state:
        cities = state.cities
        # sorted_cities = sorted(cities, key=lambda city: city.name)
        return render_template(
            "state_cities.html", state=state, cities=cities)
    else:
        return render_template("state_cities.html"), 404


@app.teardown_appcontext
def close_db(error):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
