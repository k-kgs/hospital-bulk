# Hospital Bulk Processing Service

A lightweight service to upload hospital records in bulk using CSV.  
It integrates with an existing Hospital Directory API and handles batch creation and activation.

## Features

- Bulk hospital upload via CSV
- Automatic batch ID generation
- Hospitals created inactive and activated together
- Per-row success and failure reporting
- Batch status tracking
- Swagger API documentation

## Tech Stack

- Python 3.10+
- FastAPI
- httpx
- In-memory storage
- Deployed on Render

## APIs

### Health Check  
`GET /health`

### Bulk Upload  
`POST /hospitals/bulk`

- Multipart form-data CSV upload  
- Maximum 20 hospitals per file  
- Required columns: name, address  
- Optional column: phone  

### Batch Status  
`GET /hospitals/bulk/{batch_id}/status`

## CSV Format

```csv
name,address,phone
General Hospital,123 Main St,555-1111
City Clinic,45 Park Ave,555-2222
Community Care,78 Lake Road,555-3333
```


## Run Locally
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```


## Swagger UI available at
http://127.0.0.1:8000/docs

## Deployed Version on render
https://hospital-bulk-paribus.onrender.com/docs

## Testing
GET endpoints tested using pytest

## Future Scope
Can be extended with queue based workers for production use