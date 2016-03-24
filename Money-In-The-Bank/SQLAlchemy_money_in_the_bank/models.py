from base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)
    salt = Column(String)
    balance = Column(Float, default=0)
    message = Column(String)


class LoginAttempt(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    attempt_status = Column(String)
    time = Column(DateTime)
    cleint = relationship(Client, backref="login_attempts")


class BlockedUser(Base):
    __tablename__ = "blocked_users"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    block_start = Column(DateTime)
    block_end = Column(DateTime)
    cleint = relationship("Client", backref="blocked_users")
