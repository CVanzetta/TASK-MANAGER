"""
Unit tests for Task Manager backend
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db import Base, get_db
from app.models import Task

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override database dependency for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    """Create tables before each test and drop after"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_read_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_create_task():
    """Test creating a new task"""
    task_data = {
        "title": "Test Task",
        "description": "This is a test task"
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert "id" in data
    assert data["completed"] is False


def test_read_tasks():
    """Test reading all tasks"""
    # Create a task first
    task_data = {"title": "Test Task", "description": "Test description"}
    client.post("/tasks/", json=task_data)

    # Read all tasks
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_read_task():
    """Test reading a single task"""
    # Create a task
    task_data = {"title": "Test Task", "description": "Test description"}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    # Read the task
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == task_data["title"]


def test_update_task():
    """Test updating a task"""
    # Create a task
    task_data = {"title": "Test Task", "description": "Test description"}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    # Update the task
    update_data = {
        "title": "Updated Task",
        "description": "Updated description",
        "completed": True
    }
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["completed"] is True


def test_delete_task():
    """Test deleting a task"""
    # Create a task
    task_data = {"title": "Test Task", "description": "Test description"}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    # Delete the task
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    # Verify it's deleted
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_read_nonexistent_task():
    """Test reading a task that doesn't exist"""
    response = client.get("/tasks/9999")
    assert response.status_code == 404


def test_update_nonexistent_task():
    """Test updating a task that doesn't exist"""
    update_data = {"title": "Updated", "description": "Updated"}
    response = client.put("/tasks/9999", json=update_data)
    assert response.status_code == 404


def test_delete_nonexistent_task():
    """Test deleting a task that doesn't exist"""
    response = client.delete("/tasks/9999")
    assert response.status_code == 404


def test_create_task_without_description():
    """Test creating a task without description"""
    task_data = {"title": "Test Task"}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] is None
