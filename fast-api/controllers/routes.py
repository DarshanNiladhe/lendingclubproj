from fastapi import APIRouter, HTTPException
from typing import List
from models.model import Person

router = APIRouter()

# Sample data to mimic a database
people = [
    {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 35, "email": "bob@example.com"},
]

@router.get("/people/", response_model=List[Person])
async def read_people():
    return people

@router.get("/people/{person_id}", response_model=Person)
async def read_person(person_id: int):
    for person in people:
        if person["id"] == person_id:
            return person
    raise HTTPException(status_code=404, detail="Person not found")

