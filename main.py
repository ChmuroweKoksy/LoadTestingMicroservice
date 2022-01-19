from fastapi import FastAPI, BackgroundTasks
from routers import router
import requests

# fastapi app
app = FastAPI(
    title="LoadTest",
    description="A simple Load Testing API Service built with FastAPI",
    version="0.1"
)

app.include_router(router)






# uvicorn main:app --reload