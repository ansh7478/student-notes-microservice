# Import Pydantic BaseModel for data validation
from pydantic import BaseModel
from datetime import datetime


# Schema for creating a new note
class NoteCreate(BaseModel):
    subject: str
    title: str
    content: str


# Schema for updating an existing note
class NoteUpdate(BaseModel):
    subject: str
    title: str
    content: str


# Schema for returning note data
class NoteResponse(BaseModel):
    id: int
    subject: str
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True