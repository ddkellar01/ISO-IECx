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
    assert response.json() == {"detail": "Invalid or missing API key authorization."}

def test_authorized_access_mock():
    # Test with valid bearer token (mocking scout call or verifying header passes middleware)
    headers = {"Authorization": "Bearer test-secret"}
    response = client.post("/api/v1/scout", json={"standard_id": "9999999"}, headers=headers)
    # Should pass middleware (not 401), even if standard not found (404 or dict error)
    assert response.status_code in [200, 404]
