from pathlib import Path
import shutil
import re
import fitz
from typing import Dict
import os
import base64
import logging

from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext

from qdrant_client.models import VectorParams, Distance

from app.services.embeddings import EMBED_MODEL
from app.db.qdrant_client import qdrant_client
from app.core.config import settings


logger = logging.getLogger(__name__)


# ==============================
# OpenRouter Client (SYNC)
# ==============================

client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

MODEL_ID = "qwen/qwen2.5-vl-32b-instruct"


# ==============================
# OCR (Threaded)
# ==============================

MAX_WORKERS = 3


def process_single_page(pdf_path: str, page_num: int):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_num)

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_bytes = pix.tobytes("png")
        base64_image = base64.b64encode(img_bytes).decode("utf-8")

        logger.debug("Processing page %d", page_num + 1)

        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Transcribe all the text exactly as it appears in the image."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            temperature=0.1,
            max_tokens=4096,
        )

        doc.close()

        return page_num, response.choices[0].message.content

    except Exception as e:
        logger.exception("OCR failed on page %d: %s", page_num + 1, str(e))
        return page_num, f"[Error on page {page_num + 1}: {str(e)}]"


def process_ocr(pdf_path: str) -> str:
    if not os.path.exists(pdf_path):
        logger.error("File not found: %s", pdf_path)
        raise FileNotFoundError("File not found.")

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    doc.close()

    logger.info("Starting OCR | File=%s | Pages=%d", pdf_path, total_pages)

    results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(process_single_page, pdf_path, page_num)
            for page_num in range(total_pages)
        ]

        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda x: x[0])

    logger.info("OCR completed | File=%s", pdf_path)

    return "\n".join([text for _, text in results])


# ==============================
# Text Cleaning
# ==============================

def clean_pdf_text(text: str) -> str:
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ==============================
# Dynamic Qdrant Setup
# ==============================

def ensure_collection():
    collection_name = settings.COLLECTION_NAME

    sample_vector = EMBED_MODEL._get_text_embedding("dimension check")
    vector_size = len(sample_vector)

    logger.info("Detected embedding dimension: %d", vector_size)

    collections = qdrant_client.get_collections().collections
    existing_names = [c.name for c in collections]

    if collection_name not in existing_names:
        logger.warning("Collection not found. Creating new collection: %s", collection_name)

        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )
        return

    info = qdrant_client.get_collection(collection_name)
    existing_size = info.config.params.vectors.size

    if existing_size != vector_size:
        logger.warning("Embedding dimension mismatch. Recreating collection: %s", collection_name)

        qdrant_client.delete_collection(collection_name)

        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )
    else:
        logger.info("Collection dimension validated: %s", collection_name)


# ==============================
# Ingestion (FULLY SYNC)
# ==============================

UPLOAD_DIR = Path("uploaded_docs")


import pdfplumber

def ingest_document(file, framework: str) -> Dict:

    logger.info(
        "Document ingestion started | File=%s | Framework=%s",
        file.filename,
        framework,
    )

    UPLOAD_DIR.mkdir(exist_ok=True)
    file_location = UPLOAD_DIR / file.filename

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.debug("File saved to %s", file_location)

    ensure_collection()

    # ==========================================
    # 1️⃣ Try Digital PDF Extraction First (pdfplumber)
    # ==========================================
    logger.info("Attempting digital text extraction using pdfplumber")

    digital_text = ""

    try:
        with pdfplumber.open(file_location) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    digital_text += page_text + "\n"

        logger.debug("Digital text length: %d", len(digital_text))
        print("Digital text length: ", len(digital_text))

    except Exception as e:
        logger.exception("Digital extraction failed: %s", str(e))

    # ==========================================
    # 2️⃣ Decide Whether to Use OCR
    # ==========================================
    TEXT_THRESHOLD = 100

    if len(digital_text.strip()) < TEXT_THRESHOLD:
        print("Digital text below threshold. Falling back to OCR.")
        logger.info(
            "Digital text below threshold (%d). Falling back to OCR.",
            TEXT_THRESHOLD,
        )
        full_text = process_ocr(str(file_location))
        print("OCR text: ", full_text)
    else:
        logger.info("Using digital PDF text (OCR skipped)")
        full_text = digital_text

    logger.debug("Final extracted text length: %d", len(full_text))

    # ==========================================
    # 3️⃣ Clean Text
    # ==========================================
    cleaned_text = clean_pdf_text(full_text)

    # ==========================================
    # 4️⃣ Create Llama Document
    # ==========================================
    llama_doc = Document(
        text=cleaned_text,
        metadata={
            "file_name": file.filename,
            "framework": framework,
        },
    )

    logger.debug("Llama document created with metadata: %s", llama_doc.metadata)

    # ==========================================
    # 5️⃣ Chunking
    # ==========================================
    node_parser = SentenceSplitter(
        chunk_size=1024,
        chunk_overlap=100,
    )

    nodes = node_parser.get_nodes_from_documents([llama_doc])

    logger.info("Document split into %d nodes", len(nodes))

    for node in nodes:
        node.metadata.update({
            "file_name": file.filename,
            "framework": framework,
        })

    # ==========================================
    # 6️⃣ Insert into Qdrant
    # ==========================================
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=settings.COLLECTION_NAME,
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex(
        nodes=[],
        storage_context=storage_context,
        embed_model=EMBED_MODEL,
    )

    logger.info("Inserting %d nodes into Qdrant", len(nodes))
    index.insert_nodes(nodes)

    logger.info("Document ingestion completed | File=%s", file.filename)

    return {
        "status": "success",
        "file_name": file.filename,
        "framework": framework,
        "chunks_indexed": len(nodes),
    }

