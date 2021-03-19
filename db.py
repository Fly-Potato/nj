from nonebot import on_startup
import aiofiles.os
import os.path
from nj.config import DB_FILE
from sqlalchemy.ext.asyncio import create_async_engine
import aiosqlite
from sqlalchemy.dialects import registry
registry.register("sqlite.aiosqlite", "nj.db", "aio_sqlite")


aio_sqlite = aiosqlite


@on_startup
async def init_db():
    engine = create_async_engine(f'sqlite+aiosqlite:///{DB_FILE}')

    print("start up")
