from fastapi import FastAPI
from .core.config import Settings
from .core.database import engine
from .api.routes.user import router as user_router
from .models.BaseModel import Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield
    
    await engine.dispose()


settings = Settings()
app = FastAPI(lifespan=lifespan)

app.include_router(user_router)