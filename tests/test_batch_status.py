from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_batch_status_not_found():
    fake_batch_id = "non-existent-batch-id"
    response = client.get(f"/hospitals/bulk/{fake_batch_id}/status")

    assert response.status_code == 404
    assert response.json()["detail"] == "Batch not found"
