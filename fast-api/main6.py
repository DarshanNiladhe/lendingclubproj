# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.department_controller import router as department_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include department router
app.include_router(department_router, prefix="/api/v1")
