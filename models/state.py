#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """returns the list of City instances with
        state_id equals to the current State.id"""
        matching_cities = []
        city_instances = storage.all().values()
        for city in city_instances:
            if city.state_id == self.id:
                matching_cities.append(city)
        return matching_cities
