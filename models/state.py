#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", backref="state", cascade="all, delete")
    else:
        # For FileStorage
        @property
        def cities(self):
            """Lists instances of City with state_id == to current State.id"""
            from models import storage
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
