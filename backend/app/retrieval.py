from pathlib import Path
import chromadb

import os
import requests

from dotenv import load_dotenv

load_dotenv()


HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = (
    "https://api-inference.huggingface.co/"
    "pipeline/feature-extraction/"
    "sentence-transformers/all-MiniLM-L6-v2"
)

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def get_embedding(text: str):

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": text},
        timeout=30,
    )

    return response.json()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw"

client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collection = client.get_or_create_collection(
    name="guided_curriculum"
)

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

def chunk_text(text, chunk_size=300):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])

    return chunks


# ---------------------------------------------------
# Ingestion
# ---------------------------------------------------

def ingest_documents():
    documents = load_documents()

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for index, chunk in enumerate(chunks):
            query_embedding = get_embedding(query)

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

    print("\nRetrieved Results:\n")

    for item in results["documents"][0]:
        print(item)
        print("-" * 50)