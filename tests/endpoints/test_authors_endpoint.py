from uuid import uuid4
import pytest
from starlette.testclient import TestClient

from app.models.author import AuthorCreateModel


@pytest.fixture(scope="module")
def prepared_author(test_client: TestClient) -> AuthorCreateModel:
    author = generate_author()
    test_client.post("/api/v1/authors", json=author.dict())
    return author


def test_get_authors(test_client: TestClient, prepared_author: AuthorCreateModel):
    response = test_client.get("/api/v1/authors")

    assert response.status_code == 200
    all_authors = response.json()
    assert prepared_author.first_name in [author["first_name"] for author in all_authors]
    assert prepared_author.last_name in [author["last_name"] for author in all_authors]


def test_create_authors(test_client: TestClient):
    response = test_client.post("/api/v1/authors", json=generate_author().dict())

    assert response.status_code == 201


def generate_author() -> AuthorCreateModel:
    return AuthorCreateModel(first_name=str(uuid4()), last_name=str(uuid4()))
