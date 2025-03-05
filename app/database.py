from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Определяем, какой .env файл используется
environment = os.getenv('ENVIRONMENT')

logger.info(f"Загружаем среду: {environment}")

# Определяем, какой .env файл загружать
if environment == 'docker':
    a = load_dotenv(dotenv_path=".env.docker")  # Для Docker-среды
else:
    a = load_dotenv(dotenv_path=".env.local")  # Для локальной разработки

# Загружаем параметры из переменных окружения
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Определяем, какие переменные собрали
logger.info(f"Пользователь: {POSTGRES_USER}")
logger.info(f"Пароль: {POSTGRES_PASSWORD}")
logger.info(f"Хост: {POSTGRES_HOST}")
logger.info(f"Порт: {POSTGRES_PORT}")
logger.info(f"БД: {POSTGRES_DB}")

# Формируем строку подключения к базе данных
DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)

logger.info(f"WELCOME ON BOARD, DEAR CAPTAIN! Your Database URL: {DATABASE_URL}")

# Создаем движок SQLAlchemys
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()