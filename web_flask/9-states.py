#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Lists all the states in the states list"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays a state and its cities if found"""
    state = None
    for obj in storage.all(State).values():
        if obj.id == id:
            state = obj
            break

    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template(
            "9-states.html", state=state, cities=cities)
    else:
        return render_template("9-states.html")


@app.teardown_appcontext
def close_db(error):
    """Closes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
