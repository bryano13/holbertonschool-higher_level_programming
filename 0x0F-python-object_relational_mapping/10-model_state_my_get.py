#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    to_find = sys.argv[4]
    obj = session.query(State).filter(State.name == to_find).first()
    if obj is None:
        print("Not found")
    else:
        print("{}".format(obj.id))

    session.close()
