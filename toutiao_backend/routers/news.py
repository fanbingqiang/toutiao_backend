from fastapi import APIRouter, dependencies, Depends
from sqlalchemy.orm import AsysncSession

from config.db_conf import get_db
from crud import news

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 100,db:AsysncSession = Depends(get_db())):
    categories =await news.get_categories(db,skip, limit)
    return {"code" : 200, "message" : "sucess", "data" : categories}



