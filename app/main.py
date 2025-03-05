# c_match/main.py

from fastapi import FastAPI, Form
from fastapi.openapi.models import Schema
from pydantic import BaseModel

from .database import engine, Base
from fastapi.responses import FileResponse
from fastapi import Form


app = FastAPI()

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

# Стартовая страница
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Чтение файла
@app.get("/file")
def read_html():
    return FileResponse("app/templates/index.html")

# Скачивание файла
@app.get("/file/download")
def download_file():
    return FileResponse(
        "app/templates/index.html",
        filename="mainpage.html",
        media_type="application/octet-stream"
    )
"""
Калькулятор.
Метод #1 API GET /calculator нужен для отрисовки формы ввода значений
Метод #2 API POST /calculator нужен для выполнения сложения числе
Метод #3 API POST /calc нужен для сложения через интерфейс API
"""
@app.get("/calculator", response_class=FileResponse)
def calculator_form():
    return FileResponse("app/templates/calculator.html")

@app.post("/calculator")
def calculator(num1: int = Form(), num2: int = Form()):
    print("num1 =", num1, "   num2 =", num2)
    return {"result": num1 + num2}

class numSchema(BaseModel):
    num1: int
    num2: int
@app.post("/calc")
def calc(
        body: numSchema
):
    return {"result": body.num1 + body.num2}

"""
Последующие методы расположены в app.routes

- Текущий `main.py` файл будет служить точкой входа в наше приложение FastAPI.
- Каталог "models" используется для определения моделей Pydantic для обработки проверки данных запросов и ответов.
- Каталог "routes" (маршруты) будет содержать маршруты API (конечные точки), которые определяют поведение приложения.
"""