#!/bin/python
# -*- coding: utf-8 -*-
import os
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# Database connection
DATABASE = 'sqlite:///db.sqlite3'
DEBUG = True

# Connect to database
# engine = create_engine(DATABASE, echo=DEBUG)
# session_factory = sessionmaker(bind=engine)
# session = session_factory()
#
# Base = declarative_base()

# Initialize database if it doesn't exist

def load_session():
    engine = create_engine(DATABASE, echo=DEBUG)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()
    if not os.path.exists('db.sqlite3'):
      Base.metadata.create_all(engine)

    return session

if __name__ == "__main__":
    session = load_session()
