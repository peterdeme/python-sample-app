from pydantic import BaseModel

from app.services.database import db


class ArticleBase(BaseModel):
    title: str
    body: str
    author_id: int


class ArticleInDb(db.Model):
    __tablename__ = "articles"
    id: int = db.Column(db.Integer(), primary_key=True)
    title: str = db.Column(db.String())
    body: str = db.Column(db.String())
    author_id: int = db.Column(db.Integer())


class ArticleCreateModel(ArticleBase):
    pass


class ArticleResponseModel(ArticleBase):
    id: int
