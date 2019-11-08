from pydantic import BaseModel

from app.services.database import db


class AuthorBase(BaseModel):
    first_name: str
    last_name: str


class AuthorInDb(db.Model):
    __tablename__ = "authors"
    id: int = db.Column(db.Integer(), primary_key=True)
    first_name: str = db.Column(db.String())
    last_name: str = db.Column(db.String())


class AuthorCreateModel(AuthorBase):
    pass


class AuthorResponseModel(AuthorBase):
    id: int
