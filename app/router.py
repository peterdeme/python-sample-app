from fastapi import APIRouter

from .controllers.articles import router as articles_router
from .controllers.authors import router as authors_router

app_router = APIRouter()
app_router.include_router(articles_router)
app_router.include_router(authors_router)
