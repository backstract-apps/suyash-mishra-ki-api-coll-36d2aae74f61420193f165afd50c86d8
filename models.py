from sqlalchemy import Column, Integer, String, Boolean, DateTime, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persons(Base):
    __tablename__ = 'persons'
    rollnumber = Column(Integer, primary_key=True)
    fullname = Column(String, primary_key=False)
    age = Column(Integer, primary_key=False)
    profession = Column(String, primary_key=False)

