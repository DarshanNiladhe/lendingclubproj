# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models.profile import Profile, Base
import controllers.profile_controller as profile_controller

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints
@app.post("/profiles/")
def create_profile(username: str, email: str, full_name: str, password: str, db: Session = Depends(get_db)):
    return profile_controller.create_profile(db, username, email, full_name, password)

@app.get("/profiles/{profile_id}")
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = profile_controller.get_profile(db, profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

