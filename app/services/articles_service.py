from typing import List

from app.models.article import ArticleCreateModel, ArticleInDb


class ArticleService:
    async def get_articles(self) -> List[ArticleInDb]:
        return await ArticleInDb.query.gino.all()

    async def insert_article(self, article: ArticleCreateModel) -> ArticleInDb:
        return await ArticleInDb.create(**article.dict())
