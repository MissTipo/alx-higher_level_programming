#!/usr/bin/python3
"""
    script that prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    instance = session.query(State).order_by(asc(State.id)).first()
    if instance:
        print("{:d}: {:s}".format(stmt.id, stmt.name))
    else:
        print("Nothing")
    session.close()