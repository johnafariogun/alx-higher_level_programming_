#!/usr/bin/python3
"""
    lists State objects that have the name passed as argument
    Usage: ./7-model_state_fetch_all.py <mysql username> \
                                        <mysql password> \
                                        <database name> \
                                        <state name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]

    state = session.query(State).filter_by(name=name).order_by(State.id).first()
    if state:
        print("{}".format(state.id))
    else:
        print('Not found')
