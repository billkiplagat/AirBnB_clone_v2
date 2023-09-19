#!/usr/bin/python3
""" DBStorage module for HBNB project """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import user, state, city, amenity, place, review


class DBStorage:
    """ DBStorage class for managing the database """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage instance """

        # Set environment variables
        os.environ['HBNB_MYSQL_USER'] = ''
        os.environ['HBNB_MYSQL_PWD'] = ''
        os.environ['HBNB_MYSQL_HOST'] = ''
        os.environ['HBNB_MYSQL_DB'] = ''

        db_user = os.getenv("HBNB_MYSQL_USER")
        db_pwd = os.getenv("HBNB_MYSQL_PWD")
        db_host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        db_env = os.getenv("HBNB_ENV")

        if db_env == "test":
            Base.metadata.drop_all(self.__engine)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(db_user, db_pwd,
                                              db_host, db_name),
                                      pool_pre_ping=True)
        if db_env == "test":
            return

        if (os.getenv("HBNB_MYSQL_USER") and os.getenv("HBNB_MYSQL_PWD")
                and os.getenv("HBNB_MYSQL_HOST") and os.getenv(
                "HBNB_MYSQL_DB")):
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(Session)

    def all(self, cls=None):
        """ Query objects from the database """
        result = {}
        if cls is None:
            classes = [user.User, state.State, city.City,
                       amenity.Amenity, place.Place, review.Review]
        else:
            classes = [cls]

        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """ Add object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database
        and create a new database session """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
