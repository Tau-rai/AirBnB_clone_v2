#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from os import getenv

# Defining the many-to-many relationship table
place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            nullable=False, primary_key=True),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            nullable=False, primary_key=True)
        )


class Place(BaseModel, Base):
    """Defines a class Place"""
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                'Review', cascade="all, delete, delete-orphan",
                backref='place'
                )
        amenities = relationship(
                'Amenity', secondary=place_amenity,
                viewonly=False, backref='place_amenities')
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        reviews = None
        amenities = []

        @property
        def amenities(self):
            """Returns list of Amenity instances"""
            from models import storage
            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Append an Amenity.id to the attribute amenity_ids"""
            if type(obj) is Amenity:
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)

    @property
    def reviews(self):
        """getter attribute that returns the list of Review instances with
        place_id equals to the current Place.id
        """
        from models import storage
        return [review for review in storage.all(Review).values()
                if review.place_id == self.id]
