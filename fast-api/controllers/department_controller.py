# controllers.py
from fastapi import APIRouter, HTTPException
from typing import List
from models.department import Department

router = APIRouter()

# Example data (replace with your actual data source)
departments_db = [
    {"id": 1, "name": "IT", "description": "Information Technology Department"},
    {"id": 2, "name": "HR", "description": "Human Resources Department"}
]

@router.get("/departments", response_model=List[Department])
async def get_departments():
    return departments_db

@router.get("/departments/{department_id}", response_model=Department)
async def get_department(department_id: int):
    try:
        department = next(department for department in departments_db if department["id"] == department_id)
        return department
    except StopIteration:
        raise HTTPException(status_code=404, detail="Department not found")

@router.post("/departments", response_model=Department)
async def create_department(department: Department):
    # Logic to save department data (not implemented)
    # For now, just return the received department
    return department

@router.put("/departments/{department_id}", response_model=Department)
async def update_department(department_id: int, department: Department):
    # Logic to update department data (not implemented)
    # For now, just return the received department with updated values
    return department

@router.delete("/departments/{department_id}")
async def delete_department(department_id: int):
    # Logic to delete department data (not implemented)
    # For now, just return a success message
    return {"message": f"Department with id {department_id} has been deleted"}
