#!/usr/bin/python3
"""
    script that prints the State object with the name \
            passed as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    search = argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id)

    found = False
    for i in state:
        if i.name == search:
            print("{}".format(i.id))
            found = True
            break
    if found is False:
        print("Not found")
