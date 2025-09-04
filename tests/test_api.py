import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# /search エンドポイントのテスト
def test_search():
    response = client.post("/search", json={"query": "test"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]

# /add エンドポイントのテスト
def test_add():
    response = client.post("/add", json={"data": "test"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]

# /update エンドポイントのテスト
def test_update():
    response = client.post("/update", json={"data": "test"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]

# /delete エンドポイントのテスト
def test_delete():
    response = client.post("/delete", json={"data": "test"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]
