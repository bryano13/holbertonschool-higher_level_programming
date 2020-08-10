#!/usr/bin/python3
"""Script that displays all the cities
along with their respective states from db hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user_name, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
