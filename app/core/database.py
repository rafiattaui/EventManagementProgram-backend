from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from fastapi import Request

def init_db(settings):
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
    return engine, session_maker

async def get_conn(request: Request) -> AsyncSession: # type: ignore
    session_maker = request.app.state.SESSION_LOCAL
    async with session_maker() as session:
        yield session

