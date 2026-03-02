from fastapi import APIRouter, HTTPException
from typing import List

from app.models.schemas import ValidationRequest, ComplianceResult
from app.services.compliance_service import validate_rules_service

router = APIRouter(prefix="/compliance", tags=["Compliance"])


@router.post("/validate")
async def validate_rules(request: ValidationRequest):
    try:
        results = validate_rules_service(
            framework=request.framework,
            file_name=request.file_name,
            rules=request.rules,
        )
        return results

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Validation failed: {str(e)}",
        )
