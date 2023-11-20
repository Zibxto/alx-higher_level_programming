#!/usr/bin/python3
"""
A python file that contains the class definition
of a City
"""

from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Inherits from Base class and stores records for cities"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id, back_populates="state")
