from fastapi import FastAPI

app = FastAPI(title="Hospital Bulk Processing")

@app.get("/health")
def health():
    return {"status": "ok"}
