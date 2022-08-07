#!/usr/bin/python3
"""declaring columns for a table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class state that inherits from base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
