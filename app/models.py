# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String, DateTime

# Import the Base class from database.py
from app.database import Base

# Import datetime to automatically store creation time
from datetime import datetime


# Database model representing a student note
class Note(Base):

    # Name of the database table
    __tablename__ = "notes"

    # Unique ID for every note
    id = Column(Integer, primary_key=True, index=True)

    # Subject name
    subject = Column(String, nullable=False)

    # Note title
    title = Column(String, nullable=False)

    # Main content of the note
    content = Column(String, nullable=False)

    # Store creation date automatically
    created_at = Column(DateTime, default=datetime.utcnow)