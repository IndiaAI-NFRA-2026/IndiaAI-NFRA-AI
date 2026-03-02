import json
import re
import traceback
import logging
from typing import List, Dict

from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.vector_stores.types import (
    MetadataFilters,
    MetadataFilter,
    FilterOperator,
)

from app.db.qdrant_client import qdrant_client
from app.services.embeddings import EMBED_MODEL
from app.services.llm import call_llm
from app.core.config import settings
from app.models.schemas import Rule

from llama_index.core import Settings
Settings.embed_model = EMBED_MODEL

logger = logging.getLogger(__name__)


# ----------------------------
# JSON Safety Parsing
# ----------------------------
def safe_json_parse(text: str):
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError as e:
            logger.error("JSON Decode Error: %s", str(e))
            return None
    return None


# ----------------------------
# Prompt Builder
# ----------------------------
def build_prompt(rule: Rule, framework: str) -> str:
    return f"""
You are a Senior Financial Auditor specializing in {framework}.

Strict Rules:
- Use ONLY retrieved excerpts.
- If insufficient evidence → Fail.
- Never assume disclosures.
- Never fabricate.
- Do not explain outside JSON.
- Return ONLY valid JSON.

Expected Output:
{{
  "status": "Pass" | "Fail" | "Partial",
  "explanation": "Short reasoning",
  "evidence": "Exact quoted excerpt",
  "risk": "High" | "Medium" | "Low" | "None",
  "conf": number
}}

Rule ID: {rule.rule_id}
Description: {rule.full_text}
Reference Paragraphs: {rule.mapped_paragraphs}
Rule Type: {rule.type}
"""


# ----------------------------
# Validation Service
# ----------------------------
def validate_rules_service(
    framework: str,
    file_name: str,
    rules: List[Rule],
    top_k: int = 8,
) -> List[Dict]:

    logger.info("Validation started | Framework=%s | File=%s | Rules=%d",
                framework, file_name, len(rules))

    # Check embedding dimension
    try:
        test_vec = EMBED_MODEL._get_text_embedding("dimension check")
        logger.debug("Embedding dimension: %d", len(test_vec))
    except Exception as e:
        logger.exception("Embedding dimension check failed: %s", str(e))
        raise

    # Initialize Vector Store
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=settings.COLLECTION_NAME,
    )

    from llama_index.core import StorageContext

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context,
        embed_model=EMBED_MODEL,
    )

    # Metadata Filter
    metadata_filters = MetadataFilters(
        filters=[
            MetadataFilter(
                key="file_name",
                value=file_name,
                operator=FilterOperator.EQ,
            )
        ]
    )

    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=top_k,
        filters=metadata_filters,
    )

    results = []

    # Rule Loop
    for rule in rules:

        logger.info("Validating rule: %s", rule.rule_id)

        try:
            prompt = build_prompt(rule, framework)

            logger.debug("Generated prompt for rule %s", rule.rule_id)

            # Retrieve nodes
            retrieved_nodes = retriever.retrieve(prompt)

            logger.debug("Retrieved %d nodes for rule %s",
                         len(retrieved_nodes), rule.rule_id)

            context_text = "\n\n".join(
                node.node.text for node in retrieved_nodes
            )

            final_prompt = f"""
{prompt}

Use ONLY the following retrieved excerpts:
{context_text}
"""

            raw_output = call_llm(final_prompt)

            logger.debug("Raw LLM output for rule %s: %s",
                         rule.rule_id, raw_output)

            parsed = safe_json_parse(raw_output)

            if parsed is None:
                raise ValueError("Invalid JSON returned from LLM")

        except Exception as e:
            logger.exception("Validation failed for rule %s: %s",
                             rule.rule_id, str(e))

            parsed = {
                "status": "Fail",
                "explanation": f"Validation error: {str(e)}",
                "evidence": "",
                "risk": "High",
                "conf": 0.0,
            }

        results.append(
            {
                "rule_id": rule.rule_id,
                "description": rule.description,
                "status": parsed.get("status", "Fail"),
                "explanation": parsed.get("explanation", ""),
                "evidence": parsed.get("evidence", ""),
                "risk": parsed.get("risk", "High"),
                "conf": parsed.get("conf", 0.0),
            }
        )

    logger.info("Validation completed successfully")

    return results
