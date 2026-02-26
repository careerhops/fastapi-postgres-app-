from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL running"}


@app.post("/notes", response_model=schemas.NoteResponse)
def create(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)


@app.get("/notes", response_model=list[schemas.NoteResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_notes(db)


@app.get("/notes/{note_id}", response_model=schemas.NoteResponse)
def read_one(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.delete("/notes/{note_id}")
def delete(note_id: int, db: Session = Depends(get_db)):
    note = crud.delete_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Deleted successfully"}