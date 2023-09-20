#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Table, String, ForeignKey, Float, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
from models.review import Review
from models.amenity import Amenity
from models.city import City

# Define the place_amenity table
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    PrimaryKeyConstraint('place_id', 'amenity_id')
)


class Place(BaseModel, Base):
    """
    Place Class
    """
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

    # Define the relationship for DBStorage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenity")
    # Define the getter attribute for FileStorage
    else:
        @property
        def reviews(self):
            """
            Getter attribute for reviews in FileStorage
            Returns a list of Review instances with place_id equal to the current Place.id
            """
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    @property
    def amenities(self):
        """
        Getter attribute for amenities in FileStorage
        Returns a list of Amenity instances based on amenity_ids
        """
        from models import storage
        amenity_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, amenity_obj):
        """
        Setter attribute for amenities in FileStorage
        Appends Amenity.id to amenity_ids if amenity_obj is an Amenity object
        """
        if isinstance(amenity_obj, Amenity):
            self.amenity_ids.append(amenity_obj.id)
