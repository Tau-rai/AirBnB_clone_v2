#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
import os

# place_amenity = Table('place_amenity', Base.metadata,
#         Column('place_id', String(60), ForeignKey("places.id"),
#             primary_key=True, nullable=False),
#         Column('amenity_id', String(60), ForeignKey("amenities.id"),
#             primary_key=True, nullable=False)
#         )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    amenity_ids = []
    user = relationship('User', back_populates="places")
    cities = relationship('City', back_populates="places")
    reviews = relationship('Review', backref="place", cascade="all, delete")
    # amenities = relationship(
        # 'Amenity', secondary=place_amenity,
    #  viewonly=False, back_populates="place_amenities")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """getter attribute that returns the list of Review instances with
            place_id equals to the current Place.id
            """
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]
        
        # @property
        # def amenities(self):
        #      """Returns list of Amenity instances"""
        #      from models import storage
        #      return [amenity for amenity in storage.all(Amenity).values()
        #   if amenity.id in self.amenity_ids]
        
        # @amenities.setter
        # def amenities(self, obj):
        #     """Append an Amenity.id to the attribute amenity_ids"""
        #     if type(obj) is Amenity:
        #         if obj.id not in self.amenity_ids:
        #             self.amenity_ids.append(obj.id)
