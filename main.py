from fastapi import FastAPI
from routes.interview_genrator_router import router

app = FastAPI()

app.include_router(router)