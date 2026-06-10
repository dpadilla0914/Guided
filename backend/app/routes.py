from fastapi import APIRouter

from app.retrieval import retrieve
from app.services.chat_service import process_chat
from app.logging_service import log_interaction, get_logs


router = APIRouter()


@router.post("/chat")
def chat(payload: dict):
    message = payload["message"]

    response = process_chat(message)

    system_output = response.get("response", str(response))

    log_interaction(
        user_input=message,
        system_output=system_output,
    )

    return response


@router.get("/")
def root():
    return {"message": "Guided backend running"}


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/retrieve")
def retrieval_test(query: str):
    retrieve(query)

    return {
        "query": query,
        "results": results["documents"][0],
    }


@router.get("/logs")
def logs():
    return {
        "logs": get_logs()
    }