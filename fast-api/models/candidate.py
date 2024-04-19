from pydantic import BaseModel

class Candidate(BaseModel):
    id: int
    name: str
    email: str
    skills: str

