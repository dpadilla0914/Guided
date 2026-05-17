from fastapi import APIRouter
from app.retrieval import retrieve
from app.services.chat_service import process_chat


router = APIRouter()


@router.post("/chat")
def chat(payload: dict):
    message = payload["message"]

    return process_chat(message)

@router.get("/")
def root():
    return {"message": "Guided backend running"}


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/retrieve")
def retrieval_test(query: str):
    results = retrieve(query)

    return {
        "query": query,
        "results": results["documents"][0],
    }