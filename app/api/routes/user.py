from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from ...core.database import get_conn

router = APIRouter(prefix="/user")

@router.get("/")
async def hello_users(session: AsyncSession = Depends(get_conn)):
    result = await session.execute(text("SELECT * FROM USER"))
    return result.fetchall()