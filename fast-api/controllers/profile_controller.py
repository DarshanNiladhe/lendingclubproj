# controllers/profile_controller.py

from sqlalchemy.orm import Session
from models.profile import Profile

def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def create_profile(db: Session, username: str, email: str, full_name: str, password: str):
    db_profile = Profile(username=username, email=email, full_name=full_name, password=password)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

