#!/usr/bin/env python3
""" File interpretation path """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
""" Module importation path """
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
