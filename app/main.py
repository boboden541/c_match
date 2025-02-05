# c_match/main.py

from fastapi import FastAPI
from .database import engine, Base


app = FastAPI()

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}