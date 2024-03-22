#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel):
    """An amenities class"""
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
    # Column(String(128), nullable=False)
    # from models.place import place_amenity
    # place_amenities = relationship('Place', secondary=place_amenity, 
    # viewonly=False, back_populates="amenities")
