from typing import AsyncGenerator
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite+aiosqlite:///sqlite_db/example.db"  # Для асинхронного запуска sqlite
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URI)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
Base: DeclarativeMeta = declarative_base()


# Для асинхронного запуска
async def get_async_db() -> AsyncGenerator:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        finally:
            await session.close()
