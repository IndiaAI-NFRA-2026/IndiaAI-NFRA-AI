from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from app.services.india_ai_rule_book import RULES_DB

from fastapi import APIRouter

router = APIRouter()


@router.get("/get_rules/")
async def get_framework_rules(framework_name: str):
    """
    Retrieve compliance rules for a given framework.

    Parameters:
    - framework_name: e.g., 'IND_AS_1', 'IND_AS_7', 'IND_AS_115'
    """
    # Normalize input: uppercase and remove whitespace
    clean_name = framework_name.strip().upper()

    if clean_name in RULES_DB:
        return RULES_DB[clean_name]

    raise HTTPException(
        status_code=404,
        detail=f"Framework '{clean_name}' not found. Available: {list(RULES_DB.keys())}"
    )

