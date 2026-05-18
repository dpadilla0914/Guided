from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.routes import router

from app.guardrails.detector import detect_direct_answer
from app.guardrails.rewrite import rewrite_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

class ChatRequest(BaseModel):
    question: str
    model_response: str


@app.get("/")
def root():
    return {"message": "Guided backend running"}


@app.post("/chat")
def chat(request: ChatRequest):
    flagged = detect_direct_answer(request.model_response)

    if flagged:
        final_response = rewrite_response(request.question)
    else:
        final_response = request.model_response

    return {
        "question": request.question,
        "guardrail_triggered": flagged,
        "response": final_response,
    }
