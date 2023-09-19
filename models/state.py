#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """Getter attribute to return the list of City instances with state_id equals to the current State.id"""
        from models import storage
        matching_cities = []

        # Iterate through all City instances in storage
        for city in storage.all("City").values():
            # Check if the city's state_id matches the current State's id
            if city.state_id == self.id:
                matching_cities.append(city)

        return matching_cities

