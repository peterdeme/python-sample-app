import asyncio
import pytest
from gino.api import GinoExecutor

from app.models.author import AuthorInDb
from app.services.authors_service import AuthorsService


@pytest.mark.asyncio
async def test_get_authors(monkeypatch):

    def ret_val(*args, **kwargs):
        db_ret_val = asyncio.Future()
        db_ret_val.set_result([AuthorInDb(id=1, first_name="f", last_name="l")])
        return db_ret_val

    monkeypatch.setattr(GinoExecutor, "all", ret_val)

    authors = await AuthorsService().get_authors()

    assert len(authors) == 1
    assert isinstance(authors[0], AuthorInDb)
    assert authors[0].first_name == "f"
    assert authors[0].last_name == "l"
