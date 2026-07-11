# Import Pydantic BaseModel for data validation
from pydantic import BaseModel
from datetime import datetime


# Schema for creating a new note
from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    subject: str = Field(..., min_length=2, max_length=100)
    title: str = Field(..., min_length=2, max_length=150)
    content: str = Field(..., min_length=5, max_length=2000)


# Schema for updating an existing note
class NoteUpdate(BaseModel):
    subject: str = Field(..., min_length=2, max_length=100)
    title: str = Field(..., min_length=2, max_length=150)
    content: str = Field(..., min_length=5, max_length=2000)


# Schema for returning note data
class NoteResponse(BaseModel):
    id: int
    subject: str
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True