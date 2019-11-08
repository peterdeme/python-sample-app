from typing import List
from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.models.author import AuthorCreateModel, AuthorResponseModel
from app.services.authors_service import AuthorsService

router = APIRouter()


@router.get("/api/v1/authors", response_model=List[AuthorResponseModel])
async def get(service: AuthorsService = Depends(AuthorsService)) -> List[AuthorResponseModel]:
    authors = await service.get_authors()
    return [AuthorResponseModel.parse_obj(author.to_dict()) for author in authors]


@router.post("/api/v1/authors", response_model=AuthorResponseModel, status_code=HTTP_201_CREATED)
async def post(author: AuthorCreateModel, service: AuthorsService = Depends(AuthorsService)) -> AuthorResponseModel:
    inserted = await service.insert_author(author)
    return AuthorResponseModel.parse_obj(inserted.to_dict())
