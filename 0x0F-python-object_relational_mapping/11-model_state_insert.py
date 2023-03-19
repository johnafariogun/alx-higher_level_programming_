#!/usr/bin/python3
"""
    adds a new State object from the database passed as argument
    Usage: ./11-model_state_fetch_all.py <mysql username> \
                                        <mysql password> \
                                        <database name>
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

    new_entry = State(name="Louisiana")
    session.add(new_entry)
    session.commit()
    print(new_entry.id)
