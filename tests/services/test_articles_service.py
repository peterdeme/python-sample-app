import asyncio
import pytest
from gino.api import GinoExecutor

from app.models.article import ArticleInDb
from app.services.articles_service import ArticleService


@pytest.mark.asyncio
async def test_get_articles(monkeypatch):

    def ret_val(*args, **kwargs):
        ret_val = asyncio.Future()
        ret_val.set_result([ArticleInDb()])
        return ret_val

    monkeypatch.setattr(GinoExecutor, "all", ret_val)
    articles = await ArticleService().get_articles()

    assert len(articles) == 1
    assert isinstance(articles[0], ArticleInDb)
