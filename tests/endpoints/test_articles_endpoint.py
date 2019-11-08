from uuid import uuid4
import pytest
from starlette.testclient import TestClient

from app.models.article import ArticleCreateModel


@pytest.fixture(scope="module")
def prepared_article(test_client: TestClient) -> ArticleCreateModel:
    article = generate_article()
    test_client.post("/api/v1/articles", json=article.dict())
    return article


def test_get_articles(test_client: TestClient, prepared_article: ArticleCreateModel):
    response = test_client.get("/api/v1/articles")

    assert response.status_code == 200
    assert prepared_article.title in [article["title"] for article in response.json()]


def test_create_articles(test_client: TestClient):
    response = test_client.post("/api/v1/articles", json=generate_article().dict())

    assert response.status_code == 201


def generate_article() -> ArticleCreateModel:
    return ArticleCreateModel(
        title=str(uuid4()),
        body=str(uuid4()),
        author_id=1
    )
