from sqlalchemy.orm import Session
from models.Team import TeamMember
from database import SessionLocal

def get_team_members(db: Session):
    return db.query(TeamMember).all()

def create_team_member(name: str, role: str, email: str):
    db = SessionLocal()
    new_member = TeamMember(name=name, role=role, email=email)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    db.close()
    return new_member
