from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# -----------------------------
# User
# -----------------------------
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")  # user, organizer, admin
    is_active = Column(Boolean, default=True)

# -----------------------------
# Event
# -----------------------------
class Event(Base):
    __tablename__ = "events"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    organizer_id = Column(Integer, ForeignKey("users.id"))

# -----------------------------
# Competition
# -----------------------------
class Competition(Base):
    __tablename__ = "competitions"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    date = Column(DateTime, default=datetime.utcnow)

# -----------------------------
# Payment
# -----------------------------
class Payment(Base):
    __tablename__ = "payments"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    amount = Column(Float)
    paid = Column(Boolean, default=False)

# -----------------------------
# Score
# -----------------------------
class Score(Base):
    __tablename__ = "scores"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    competition_id = Column(Integer, ForeignKey("competitions.id"))
    points = Column(Float, default=0)
