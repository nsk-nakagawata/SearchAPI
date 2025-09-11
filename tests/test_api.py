import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.config.config import API_KEY


client = TestClient(app)
headers = {"x-api-key": API_KEY}

# /search エンドポイントのテスト
def test_search():
    response = client.post("/search", json=[0.0]*1536, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]

# /add エンドポイントのテスト
def test_add():
    response = client.post("/add", json={
        "SYOCD": "01",
        "HACNO": "A1",
        "HACREN": "01",
        "embedding": [0.0]*1536
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]

# /update エンドポイントのテスト
def test_update():
    response = client.post("/update", json={
        "SYOCD": "01",
        "HACNO": "A1",
        "HACREN": "01",
        "embedding": [1.0]*1536
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]

# /delete エンドポイントのテスト
def test_delete():
    response = client.post("/delete", json={
        "SYOCD": "01",
        "HACNO": "A1",
        "HACREN": "01"
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json()["data"]
