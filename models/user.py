#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from models.base_model import Base
from os import getenv


class User(BaseModel, Base):

    __tablename__ = "users"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade='all,delete-orphan',
                              backref="user")
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
