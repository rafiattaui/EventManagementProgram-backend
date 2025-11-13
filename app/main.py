from fastapi import FastAPI
from .core.config import Settings
from .core.database import init_db, get_conn
from .api import routers
from .models import Base
from contextlib import asynccontextmanager
from functools import partial

settings = Settings()
engine, sessionLocal = init_db(settings)

get_db = partial(get_conn, sessionLocal)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.dependency_overrides[get_conn] = get_db

for r in routers:
    app.include_router(r)