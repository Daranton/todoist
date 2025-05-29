import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test task", "description": "Test desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test task"
    assert data["description"] == "Test desc"
    assert data["completed"] is False
    assert "id" in data

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    # Create a task first
    response = client.post("/tasks/", json={"title": "Update me"})
    task_id = response.json()["id"]

    # Update task
    response = client.put(f"/tasks/{task_id}", json={"completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True

