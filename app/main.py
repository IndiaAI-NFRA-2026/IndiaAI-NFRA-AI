from fastapi import FastAPI
from app.api import ingestion, compliance, rules
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(ingestion.router)
app.include_router(compliance.router)
app.include_router(rules.router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
