from fastapi import FastAPI
from controllers.team_member import get_team_members, create_team_member
from database import Base, engine
from models.Team import TeamMember

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/team_members/")
def read_team_members():
    return get_team_members()

@app.post("/team_members/")
def add_team_member(name: str, role: str, email: str):
    return create_team_member(name, role, email)
