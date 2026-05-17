from fastapi import APIRouter
from app.retrieval import retrieve

router = APIRouter()


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