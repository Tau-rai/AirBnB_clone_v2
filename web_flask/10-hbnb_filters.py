#!/usr/bin/python3
"""
This file contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Lists all the states and cities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def close_db(error):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
