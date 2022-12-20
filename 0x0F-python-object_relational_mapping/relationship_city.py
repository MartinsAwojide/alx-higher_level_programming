#!/usr/bin/python3
"""
relationship_city.py to set up City relationship in sqlalchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    relationship_city.py to set up City relationship in sqlalchemy
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
