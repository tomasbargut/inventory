import pytest
from inventory.asgi import app
from fastapi.testclient import TestClient

@pytest.fixture()
def client():
    return TestClient(app)