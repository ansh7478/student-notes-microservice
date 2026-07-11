# Import SQLAlchemy tools used to connect the application to the database
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database file used by the Student Notes Microservice
DATABASE_URL = "sqlite:///./notes.db"

# Create the connection between FastAPI and SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create a database session factory
# A new session is created whenever an API endpoint needs database access
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class used by SQLAlchemy database models
Base = declarative_base()


def get_db():
    """
    Provide a database session to FastAPI endpoints.

    The session is opened before the request and closed automatically
    after the request has finished.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()