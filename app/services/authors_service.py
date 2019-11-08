from typing import List

from app.models.author import AuthorCreateModel, AuthorInDb


class AuthorsService:
    async def get_authors(self) -> List[AuthorInDb]:
        return await AuthorInDb.query.gino.all()

    async def insert_author(self, author: AuthorCreateModel) -> AuthorInDb:
        return await AuthorInDb.create(**author.dict())
