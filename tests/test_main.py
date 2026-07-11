from fastapi.testclient import TestClient

from app.main import app


# Create a test client for the FastAPI application
client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Student Notes Microservice!"
    }


def test_create_note():
    response = client.post(
        "/notes",
        json={
            "subject": "Cloud Computing",
            "title": "Docker Test",
            "content": "This note was created during automated testing."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["subject"] == "Cloud Computing"
    assert data["title"] == "Docker Test"
    assert data["content"] == "This note was created during automated testing."
    assert "id" in data
    assert "created_at" in data


def test_get_notes():
    response = client.get("/notes")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_validation_rejects_short_input():
    response = client.post(
        "/notes",
        json={
            "subject": "A",
            "title": "B",
            "content": "Hi"
        }
    )

    assert response.status_code == 422