from llama_index.core.embeddings import BaseEmbedding
from typing import List
from pydantic import Field, PrivateAttr
from openai import OpenAI
from app.core.config import settings


class BGEEmbedding(BaseEmbedding):
    model: str = Field(default="baai/bge-large-en-v1.5")

    # 👇 THIS FIXES YOUR ERROR
    _client: OpenAI = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    def _get_query_embedding(self, query: str) -> List[float]:
        response = self._client.embeddings.create(
            model=self.model,
            input=query,
        )

        return response.data[0].embedding

    def _get_text_embedding(self, text: str) -> List[float]:
        response = self._client.embeddings.create(
            model=self.model,
            input=text,
        )

        return response.data[0].embedding

    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)

    async def _aget_text_embedding(self, text: str) -> List[float]:
        return self._get_text_embedding(text)


EMBED_MODEL = BGEEmbedding()
