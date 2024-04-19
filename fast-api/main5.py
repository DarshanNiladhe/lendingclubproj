from fastapi import FastAPI
from controllers.candidate_controller import router as candidate_router

app = FastAPI()

app.include_router(candidate_router, prefix="/api")
