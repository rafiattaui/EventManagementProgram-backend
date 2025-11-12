from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from os import getenv

engine = create_async_engine(getenv("DATABASE_URL", "mysql+asyncmy://root:1234@localhost:3306/ems"), echo=True)
session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_conn():
    async with session_maker() as session:
        yield session

