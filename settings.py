from functools import lru_cache
from typing import Literal
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Global Settings"""
    model_config = SettingsConfigDict(env_file=f'{BASE_PATH}/.env', env_file_encoding='utf-8', extra='ignore')

    # Env PostgreSQL
    POSTGRES_HOST :str
    POSTGRES_PORT: int
    POSTGRES_DB_NAME :str
    POSTGRES_USER :str
    POSTGRES_PASSWORD :str

    POSTGRESQL_ECHO: bool = False
    # MYSQL_CHARSET: str = 'utf8mb4'

    # Env Redis
    REDIS_HOST: str
    REDIS_PORT: int

    # FastAPI
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'FastAPI App'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'Product Management App'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOCS_URL: str | None = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'

    # DateTime
    DATETIME_TIMEZONE: str = 'Africa/Casablanca'


#@lru_cache
def get_settings() -> Settings:
    """method to retreive settings from the .env file"""
    return Settings()


settings = get_settings()






