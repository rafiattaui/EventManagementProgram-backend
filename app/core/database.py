from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker

def init_db(settings):
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
    return engine, session_maker

async def get_conn(session_maker):
    async with session_maker() as session:
        yield session

