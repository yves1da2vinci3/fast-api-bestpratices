from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_post():
    response = client.post("/posts/", json={"title": "Test Post", "content": "This is a test post"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"
    assert response.json()["content"] == "This is a test post"

def test_read_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
