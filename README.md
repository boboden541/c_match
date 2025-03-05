# Песочница
Приложение предназначена для обучения Python разработке
на fastApi

#### Используемый стек:
🐍 Python3.11  
🐍 FastAPI  
🐍 SQLAlchemy2  
🐍 Pydantic2  
🐍 Pytest  
🏷️ Postgres  

#### Полезные ссылки
{приложить ссылки}

# 📗 1. Запуск проекта
```bash
docker compose up -d
```
> флаг `--build` перебилдит текущий проект

## 2.2. Запуск проекта в виртуальном окружении Poetry (без Docker)
Ставим флаг `virtualenvs.in-project`, если хотим создавать .venv в  
текущей папки проекта (_опционально_)

- Активируем окружение;
```bash
source .venv/bin/activate
```

- Устанавливаем зависимости;
```bash
poetry install 
```
- Ставим pre-commit для линта кода;
```bash
pre-commit install
```
- Ставим pre-commit для gitlint;
```bash
pre-commit install --hook-type commit-msg
```
- Запуск проекта
```bash
uvicorn app.main:app --reload
```
# 📗 2.  Структура проекта
- ## 🗂️ [app](./app/README.md) 
Приложение
- ### 🗂️ [app/main.py](./app/README.md) 
Основная точка входа в приложение FastApi
- ### 🗂️ [app/routes](./app/README.md) 
Маршруты API
- ### 🗂️ [app/models](./app/README.md) 
Определение моделей Pydantic для работы с API


# 📗 3. Дополнительная информация  Работа c Makefile

## 3.1 Работа c Makefile - TODO

`Makefile` это удобный способ назначать короткие для запоминания имена для  "длинных"
команд.
К примеру есть команда `alembic upgrade head`, которая применяет миграцию. Для нее можно
назначить удобное короткое,  
для запоминания имя в файле `Makefile`: