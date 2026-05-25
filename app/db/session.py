from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL, 
    echo=True, 
    future=True,
    connect_args={"ssl": False}, 
    pool_pre_ping=True,   
    pool_recycle=3600   
)

AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)
