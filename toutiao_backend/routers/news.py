from email.mime import image
from fastapi import HTTPException

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from crud import news

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    categories =await news.get_categories(db,skip, limit)
    return {"code" : 200, "message" : "sucess", "data" : categories}

@router.get("/list")
async def get_news_list(
        category_id: int = Query(..., alias="categoryId"),
        page: int = 1,
        page_size: int = Query(10, alias="pageSize",le = 100),
        db: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * page_size
    news_list = await news.get_news_list(db,category_id,offset,page_size)
    total = await news.get_news_count(db,category_id)
    has_more = (offset + len(news_list))<total
    return {"code" : 200, "message" : "sucess","data":{"list":news_list,"total":total,"hasMore":has_more}}

@router.get("/detail")
async def get_news_detail(news_id: int = Query(...,alias="id"), db: AsyncSession = Depends(get_db)):
    #NEWS详情 浏览+1 相关新闻
    news_detail = await news.get_news(db,news_id)
    if news_detail is None:
        raise HTTPException(status_code=404, detail="news not found")

    views_res = await news.increase_news_views(db,news_detail.id)
    if views_res is None:
        raise HTTPException(status_code=404, detail="news not found")

    related_news = await news.get_related_news(db,news_detail.id,news_detail.category_id)



    return {"code" : 200, "message" : "sucess","data":{"id":news_detail.id,"title":news_detail.title,"content":news_detail.content,"image" : news_detail.image,"author":news_detail.author,"publishTime":news_detail.publishTime,"categoryId":news_detail.category_id,"view":news_detail.views,"relatedNews":related_news}}




