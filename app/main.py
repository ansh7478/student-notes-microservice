from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import Base, engine, get_db
from app import schemas, crud, models

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Notes Microservice",
    description="Cloud Computing Summer Semester 2026",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to Student Notes Microservice!"}


@app.post("/notes", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)


@app.get("/notes", response_model=List[schemas.NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)


@app.get("/notes/{note_id}", response_model=schemas.NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note


@app.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    updated_note = crud.update_note(db, note_id, note)

    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")

    return updated_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted_note = crud.delete_note(db, note_id)

    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note deleted successfully"}