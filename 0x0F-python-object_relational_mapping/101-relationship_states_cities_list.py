#!/usr/bin/python3
"""
101-relationship_states_cities_list.py - list State and City objects
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # select states.id, states.name, cities.id, cities.name from cities
    # join states on cities.state_id=states.id;
    rows = session.query(State).all()
    for s in rows:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("    {}: {}".format(c.id, c.name))

    session.close()
