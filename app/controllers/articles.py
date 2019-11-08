from typing import List
from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.models.article import ArticleCreateModel, ArticleResponseModel
from app.services.articles_service import ArticleService

router = APIRouter()


@router.get("/api/v1/articles", response_model=List[ArticleResponseModel])
async def get(service: ArticleService = Depends(ArticleService)) -> List[ArticleResponseModel]:
    articles = await service.get_articles()
    return [ArticleResponseModel.parse_obj(article.to_dict()) for article in articles]


@router.post("/api/v1/articles", response_model=ArticleResponseModel, status_code=HTTP_201_CREATED)
async def post(article: ArticleCreateModel, service: ArticleService = Depends(ArticleService)) -> ArticleResponseModel:
    inserted = await service.insert_article(article)
    return ArticleResponseModel.parse_obj(inserted.to_dict())
