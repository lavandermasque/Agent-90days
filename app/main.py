from fastapi import FastAPI
from app.routers import demo

app = FastAPI()
app.include_router(demo.router)