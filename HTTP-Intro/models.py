from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base
from sqlalchemy.orm import relationship


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)


class Airline(Base):
    __tablename__ = "airlines"
    id = Column(Integer, primary_key=True)
    country = Column(String, ForeignKey(Country.id))
    amount = Column(Integer)
    code = relationship(Country, backref="cd")
