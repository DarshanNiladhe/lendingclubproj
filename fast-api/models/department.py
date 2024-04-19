# models.py
from pydantic import BaseModel

class Department(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
