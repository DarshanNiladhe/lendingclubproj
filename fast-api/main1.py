from fastapi import FastAPI, HTTPException
from controllers.recuriter_controller import register_recruiter
from models.recuriter import Recuriter

app = FastAPI()

@app.post("/register/")
async def register(recruiter: Recuriter):
    try:
        registered_recruiter = await register_recruiter(recruiter)
        return {"message": "Recruiter registered successfully", "data": registered_recruiter}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
