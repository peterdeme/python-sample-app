from pathlib import Path
import pytest
from starlette.testclient import TestClient

from alembic.command import upgrade
from alembic.config import Config
from app.app import app


@pytest.fixture(scope="session", autouse=True)
def run_alembic_migrations():
    alembic_ini_path = Path.joinpath(Path(__file__).resolve().parents[1], "alembic.ini")
    alembic_conf = Config(str(alembic_ini_path))
    upgrade(alembic_conf, "head")


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    test_client = TestClient(app)
    with test_client:
        yield test_client
