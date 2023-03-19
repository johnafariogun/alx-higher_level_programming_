#!/usr/bin/python3
"""
this module declares a state class which inherits a Base instance
to be mapped to a MySQL database table
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        This simply represents a MySQL database

        __tablename__ (str): the name of the MySQL table to store the States
        id (sqlalchemy.Integer): state id
        name (sqlalchemy.String): state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
