#!/usr/bin/python3
"""This module handles the database storage"""


import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.city import City
from models.review import Review


class DBStorage:
    """The Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatiates class attributes"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )

        if os.getenv('HBNB_ENV') == "test":
            # drop all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current db session all objects depending on class name"""
        objects_dict = dict()
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects_dict[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects_dict[obj_key] = obj
        return objects_dict

    def new(self, obj):
        """Adds objects to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current db session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the db and the current db sesssion"""
        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
