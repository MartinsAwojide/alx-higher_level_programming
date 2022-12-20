#!/usr/bin/python3
"""
Print the first State object from the database hbtn_0e_6_usa or print
the text, Nothing, if table is empty
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        a = session.query(State).first()
        print("1: {}".format(a.name))
    except:
        print("Nothing")
