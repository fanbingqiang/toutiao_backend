from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.orm import AsysncSession
from models.news import Category

async def get_categories(db,skip:int = 0, limit:int = 100):
    stmt = select(Category).offset(skip).limit(limit)
    result = await db.execute(stmt)
    categories = result.scalars().all()


