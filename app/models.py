# Import database column types
from sqlalchemy import Column, Integer, String, DateTime

# Import Base from database.py
from app.database import Base

# Import datetime for created date
from datetime import datetime


# Note table model
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)