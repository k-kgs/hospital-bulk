import httpx

BASE_URL = "https://hospital-directory.onrender.com"

class HospitalClient:
    def __init__(self):
        self._client = httpx.Client(timeout=30)

    def create_hospital(self, data):
        response = self._client.post(
            f"{BASE_URL}/hospitals/",
            json=data
        )
        response.raise_for_status()
        return response.json()

    def activate_batch(self, batch_id):
        response = self._client.patch(
            f"{BASE_URL}/hospitals/batch/{batch_id}/activate"
        )
        response.raise_for_status()
