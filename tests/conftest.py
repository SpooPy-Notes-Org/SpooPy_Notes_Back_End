import pytest
from app import create_app
from config import Config


class TestConfig(Config):
    pass

@pytest.fixture
def client():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()

    with app.test_client() as client:
        yield client

    app_context.pop()