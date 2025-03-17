from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Daksh-DevOps!"}

def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_create_item():
    new_item = {"name": "Tablet", "price": 299.99, "description": "A new tablet"}
    response = client.post("/items/3", json=new_item)
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "Tablet"

def test_delete_item():
    response = client.delete("/items/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
