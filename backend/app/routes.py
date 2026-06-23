from fastapi import APIRouter
from pydantic import BaseModel

from app.retrieval import retrieve
from app.services.chat_service import process_chat
from app.logging_service import log_interaction, get_logs


class ChatRequest(BaseModel):
    message: str


router = APIRouter()


@router.post("/chat")
def chat(payload: ChatRequest):

    message = payload.message

    response = process_chat(message)

    system_output = response.get("response", "")

    log_interaction(
        user_input=message,
        system_output=system_output,
        intent=response.get("intent"),
        struggling=response.get("struggling"),
        topic=response.get("topic"),
    )

    return {
        "response": response.get("response")
    }


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


@router.get("/logs")
def logs():
    return {
        "logs": get_logs()
    }