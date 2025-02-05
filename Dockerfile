# Выбор менее прожорливого образа
FROM python:3.11-slim-bullseye
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    # переопределяем стандартное расположение poetry, чтобы в дальнейшем использовать
    POETRY_HOME="/usr/local/bin/poetry" \
    # создаст venv в PROJECT_PATH
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.8.3 \
    PROJECT_PATH="/app"
ENV PATH="$POETRY_HOME/bin:$PATH"
# Установка CURL
RUN apt-get -y update
RUN apt-get -y install curl
# Создание рабочей директории
WORKDIR $PROJECT_PATH
# Копирование файлов
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry=="$POETRY_VERSION" && poetry install

COPY ./app ./app
COPY ./alembic.ini ./
COPY ./alembic ./alembic