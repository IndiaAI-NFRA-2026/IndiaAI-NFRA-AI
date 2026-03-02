from qdrant_client import QdrantClient
from app.core.config import settings

qdrant_client = QdrantClient(path=settings.QDRANT_PATH)
