import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Service running"

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json
    assert len(response.json["version"]) > 0
