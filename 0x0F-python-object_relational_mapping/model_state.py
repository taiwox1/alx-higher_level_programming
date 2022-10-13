#!/usr/bin/python3

""" the file contain the defination of a state and an instancr
    Base = declarative_base():
        state class:\
                inherits from Base Tips\
                links to the MySQL table states\
                id : interger  that represents a column of an\
                auto-generated,
    name: represents a column of a string with\
            maximum 128 characters and can’t be null
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
         name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)