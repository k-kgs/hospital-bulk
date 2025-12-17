from fastapi import FastAPI
from app.api.bulk import router as bulk_router

app = FastAPI(title="Hospital Bulk Processing")

app.include_router(bulk_router)

@app.get("/health")
def health():
    return {"status": "ok"}
