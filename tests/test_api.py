"""Integration tests for FastAPI endpoints using TestClient."""
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "ISO-IECx Core"}

def test_unauthorized_access():
    response = client.post("/api/v1/scout", json={"standard_id": "27001"})
    assert response.status_code == 401
