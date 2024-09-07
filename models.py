from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import date, time


class Movie(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., max_length=500)
    genre: str = Field(..., max_length=40)
    actors: Optional[List[str]] = None

    class Config:
        orm_mode = True  # совместимость с ORM


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=2, max_length=25, description="Username must be between 2 and 25 characters.")
    email: EmailStr
    date_of_birth: Optional[date] = None

    @validator('username')
    def format_username(cls, value):
        value = ' '.join(word.capitalize() for word in value.split())
        return value

    class Config:
        orm_mode = True


class Ticket(BaseModel):
    id: int
    user_id: int
    movie_id: int
    seat: int
    date: date
    time: time

    class Config:
        orm_mode = True
