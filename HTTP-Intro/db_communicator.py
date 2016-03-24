import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from base import Base
from models import Airline, Country
import requests

engine = create_engine("sqlite:///airlines.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('country_histogram.json', 'r') as f:
    data = json.load(f)

airlines = [Airline(country=key, amount=int(data[key])) for key in data]

session.add_all(airlines)
session.commit()

r = requests.get("http://data.okfn.org/data/core/country-list/r/data.json")
countries = [Country(name=c["Name"], code=c["Code"])
             for c in r.json()]

session.add_all(countries)
session.commit()
