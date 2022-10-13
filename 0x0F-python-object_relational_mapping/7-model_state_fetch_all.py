#!/usr/bin/python3

"""
    script that lists all State objects from the database hbtn_0e_6_usa.
    Usage: ./7-model_state_fetch_all.py <mysql username> /
                                     <mysql password> /
                                     <database name>

"""
from sys import argv
import sqlalchemy
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_state = session.query(State).order_by(State.id).all()
    for state in query_state:
        print("{}: {}".format(state.id, state.name))