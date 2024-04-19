from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample data for organization chart
org_chart_data = {
    1: {"name": "CEO", "manager_id": None},
    2: {"name": "CTO", "manager_id": 1},
    3: {"name": "CFO", "manager_id": 1},
    4: {"name": "Manager 1", "manager_id": 2},
    5: {"name": "Manager 2", "manager_id": 2},
    6: {"name": "Employee 1", "manager_id": 4},
    7: {"name": "Employee 2", "manager_id": 4},
}


class Employee(BaseModel):
    id: int
    name: str
    manager_id: int


class OrganizationChart(BaseModel):
    employees: List[Employee]


@app.get("/org-chart/{employee_id}", response_model=OrganizationChart)
async def get_org_chart(employee_id: int):
    if employee_id not in org_chart_data:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee = org_chart_data[employee_id]
    subordinates = [emp for emp in org_chart_data.values() if emp["manager_id"] == employee_id]

    employees = [Employee(id=key, name=value["name"], manager_id=value["manager_id"]) for key, value in
                 org_chart_data.items() if value["manager_id"] == employee_id]

    return {"employees": employees}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
