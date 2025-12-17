import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.csv_reader import read_csv
from app.storage.batch_store import save_batch, get_batch

router = APIRouter()


@router.post("/hospitals/bulk")
def bulk_upload(file: UploadFile = File(...)):
    try:
        rows = read_csv(file.file.read())
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    from app.models.batch import Batch
    from app.services.hospital_client import HospitalClient

    batch_id = str(uuid.uuid4())
    batch = Batch(batch_id, len(rows))
    save_batch(batch)

    client = HospitalClient()

    for idx, row in enumerate(rows, start=1):
        payload = {
            "name": row.get("name"),
            "address": row.get("address"),
            "phone": row.get("phone"),
            "creation_batch_id": batch_id
        }

        try:
            try:
                result = client.create_hospital(payload)
            except Exception:
                result = client.create_hospital(payload)

            batch.processed += 1
            batch.results.append({
                "row": idx,
                "hospital_id": result["id"],
                "name": result["name"],
                "status": "created"
            })

        except Exception as exc:
            batch.failed += 1
            batch.results.append({
                "row": idx,
                "name": row.get("name"),
                "status": "failed",
                "error": str(exc)
            })

    if batch.processed > 0:
        try:
            client.activate_batch(batch_id)
            batch.activated = True
        except Exception:
            batch.activated = False

    return {
        "batch_id": batch_id,
        "total_hospitals": batch.total,
        "processed_hospitals": batch.processed,
        "failed_hospitals": batch.failed,
        "batch_activated": batch.activated,
        "hospitals": batch.results
    }


@router.get("/hospitals/bulk/{batch_id}/status")
def batch_status(batch_id: str):
    batch = get_batch(batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")

    return {
        "batch_id": batch.batch_id,
        "total": batch.total,
        "processed": batch.processed,
        "failed": batch.failed,
        "activated": batch.activated
    }
