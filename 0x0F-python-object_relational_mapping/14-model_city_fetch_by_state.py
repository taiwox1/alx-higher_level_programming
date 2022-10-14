#!/usr/bin/python3

"""
    script prints all the city objects from the database hbtn_0e_14_usa
    script takes 3 arguments: <mysql username>, <mysql password>\
            <database name>
"""

import sqlalchemy
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    session = Session()
    City_list = session.query(City).order_by(City.id).all()

    for city in City_list:
        print("{}: {} {}".format(City.state_id, City.id, City.name))
