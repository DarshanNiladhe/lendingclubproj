from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RecuriterLogin(BaseModel):
    username: str
    password: str

# Sample hardcoded credentials for demonstration purposes
valid_credentials = {"admin": "password123"}  # Replace with actual credentials lookup logic

@app.post("/login/")
async def login(recruiter_login: RecuriterLogin):
    # Check if the provided username exists in the valid_credentials dictionary
    if recruiter_login.username in valid_credentials:
        # Check if the provided password matches the stored password for the username
        if recruiter_login.password == valid_credentials[recruiter_login.username]:
            # Authentication successful
            return {"message": "Login successful"}
        else:
            # Invalid password
            raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        # Invalid username
        raise HTTPException(status_code=401, detail="Invalid username or password")
