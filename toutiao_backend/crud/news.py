from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession, result
from models.news import NewsCategory, News


async def get_categories(db,skip:int = 0, limit:int = 100):
    stmt = select(NewsCategory).offset(skip).limit(limit)
    result = await db.execute(stmt)
    categories = result.scalars().all()
    return categories

async def get_news_list(db: AsyncSession,category_id:int,skip:int = 0, limit:int = 10):
    #查指定分类下的新闻
    stmt = select(News).where(News.category_id==category_id).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_news_count(db: AsyncSession,category_id:int):
    stmt = select(func.count(News.id)).where(News.category_id==category_id)
    result = await db.execute(stmt)
    return result.scalar_one()

async def get_news_detail(db: AsyncSession,news_id:int):
    stmt = select(News).where(News.id==news_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def increase_news_views(db: AsyncSession,news_id:int):
    update(News).where(News.id == news_id).values(views=News.views+1)
    result = await db.execute(update)
    await db.commit()

    #检查是否真的+1了
    return result.rowcount > 0

async def get_related_news(db: AsyncSession,category_id:int,news_id:int,limit:int=5):
    stmt = select(News).where(News.category_id==category_id,News.id != news_id).order_by(News.views.desc(),News.publish_time.desc()).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

