from pathlib import Path

import os
import requests
import chromadb

from dotenv import load_dotenv

load_dotenv()


JINA_API_KEY = os.getenv("JINA_API_KEY")

API_URL = "https://api.jina.ai/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {JINA_API_KEY}",
    "Content-Type": "application/json",
}

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw"


client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collection = client.get_or_create_collection(
    name="guided_curriculum"
)

def get_embedding(text: str):

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={
            "input": [text],
            "model": "jina-embeddings-v2-base-en",
        },
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    return data["data"][0]["embedding"]

# Load curriculum files
# ---------------------------------------------------

def load_documents():
    documents = []

    for file_path in DATA_PATH.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "id": file_path.stem,
                "text": text,
            }
        )

    return documents


# ---------------------------------------------------
# Chunking
# ---------------------------------------------------

def chunk_text(text, max_chunk_size=1000):

    paragraphs = text.split("\n\n")

    chunks = []

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        # Split oversized paragraphs
        if len(paragraph) > max_chunk_size:

            for i in range(0, len(paragraph), max_chunk_size):
                chunks.append(
                    paragraph[i:i + max_chunk_size]
                )

        else:
            chunks.append(paragraph)

    return chunks


# ---------------------------------------------------
# Ingestion
# ---------------------------------------------------

def ingest_documents():

    existing_count = collection.count()

    if existing_count > 0:
        print("Documents already ingested.")
        return
    documents = load_documents()

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for index, chunk in enumerate(chunks):
            query_embedding = get_embedding(chunk)

            collection.add(
                ids=[f"{doc['id']}_{index}"],
                documents=[chunk],
                embeddings=[query_embedding],
                metadatas=[{"source": doc["id"]}],
            )

    print("Ingestion complete.")

# ---------------------------------------------------
# Retrieval
# ---------------------------------------------------

def retrieve(query, top_k=3):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results


# ---------------------------------------------------
# Local test
# ---------------------------------------------------

if __name__ == "__main__":
    ingest_documents()

    query = "How do Python loops work?"

    results = retrieve(query)