#!/bin/python
# -*- coding: utf-8 -*-
#from sqlalchemy.orm import sessionmaker
from settings import database
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

class UserPermissions(Base):
    __tablename__ = 'user_permission'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey=('user_id'))
    user = relationship(
        User,
        backref=backref('users',
                        uselist=True,
                        cascade='delete,all'))


