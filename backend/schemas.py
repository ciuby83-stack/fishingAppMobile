# schemas.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_organizer: bool
    is_admin: bool

    class Config:
        orm_mode = True

class EventCreate(BaseModel):
    name: str

class CompetitionCreate(BaseModel):
    name: str

from pydantic import BaseModel

class EventCreate(BaseModel):
    name: str
    description: str
    organizer_id: int

class EventOut(BaseModel):
    id: int
    name: str
    description: str
    organizer_id: int

    class Config:
        orm_mode = True

class CompetitionCreate(BaseModel):
    name: str
    event_id: int
    max_participants: int | None = None

class CompetitionOut(BaseModel):
    id: int
    name: str
    event_id: int
    max_participants: int | None

    class Config:
        orm_mode = True

class ScoreCreate(BaseModel):
    user_id: int
    competition_id: int
    points: float

class ScoreOut(BaseModel):
    id: int
    user_id: int
    competition_id: int
    points: float

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str | None = "user"  # implicit user

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        orm_mode = True
