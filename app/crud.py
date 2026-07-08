from sqlalchemy.orm import Session
from app import models, schemas

# Create a new note
def create_note(db: Session, note: schemas.NoteCreate):
    new_note = models.Note(
        subject=note.subject,
        title=note.title,
        content=note.content
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

# Get all notes
def get_notes(db: Session):
    return db.query(models.Note).all()


# Get one note by ID
def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

# Update a note
def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    existing_note = get_note(db, note_id)

    if existing_note:
        existing_note.subject = note.subject
        existing_note.title = note.title
        existing_note.content = note.content

        db.commit()
        db.refresh(existing_note)

    return existing_note

# Delete a note
def delete_note(db: Session, note_id: int):
    existing_note = get_note(db, note_id)

    if existing_note:
        db.delete(existing_note)
        db.commit()

    return existing_note