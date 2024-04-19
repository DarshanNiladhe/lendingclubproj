from fastapi import FastAPI
from controllers.routes import router as people_router

app = FastAPI()

app.include_router(people_router)


