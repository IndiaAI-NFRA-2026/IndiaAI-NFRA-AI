from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.ingestion_service import ingest_document

router = APIRouter(prefix="/ingestion", tags=["Ingestion"])


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    framework: str = Form(...)
):
    try:
        result = ingest_document(file=file, framework=framework)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ingestion failed: {str(e)}"
        )
