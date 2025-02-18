import pytest
from dotenv import load_dotenv

from app.app import app


@pytest.fixture(scope="module")
def app():
    """Creates Flask App instance"""
    
    load_dotenv()
    app.config.update({"TESTING": True})

    yield app


@pytest.fixture
def client(app):
    """Creates a test client"""
    
    return app.test_client()
