"""数据库配置"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class DBConfig:
    """数据库连接配置"""
    HOST = "localhost"
    PORT = 3306
    USER = "root"
    PASSWORD = "asdfghjkl123"
    DATABASE = "news_app"
    CHARSET = "utf8mb4"


# 异步引擎
ASYNC_SQLALCHEMY_URL = f"mysql+aiomysql://{DBConfig.USER}:{DBConfig.PASSWORD}@{DBConfig.HOST}:{DBConfig.PORT}/{DBConfig.DATABASE}?charset={DBConfig.CHARSET}"
engine = create_async_engine(ASYNC_SQLALCHEMY_URL, echo=False)

# 异步会话工厂
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    """FastAPI 依赖：获取数据库会话"""
    async with async_session() as session:
        yield session