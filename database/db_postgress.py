from contextlib import asynccontextmanager
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from settings import settings


def create_engine_and_session(url: str | URL):
    try:
        engine = create_async_engine(
            url,
            echo=settings.POSTGRESQL_ECHO,
            future=True,
            pool_pre_ping=True,
        )
    except Exception as e:
        raise e
    else:
        session = async_sessionmaker(bind=engine,
                             autoflush=False,
                             expire_on_commit=False)
        return engine, session    


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}"
    f":{settings.POSTGRES_PORT}/{settings.POSTGRES_DB_NAME}"
)


async_engine, async_session  = create_engine_and_session(
    SQLALCHEMY_DATABASE_URL)




