from app.retrieval import retrieve
from app.guardrails.detector import detect_direct_answer


def process_chat(message: str):

    # INPUT GUARDRAIL
    if detect_direct_answer(message):
        return {
            "response": (
                "I can help guide you through the problem, "
                "but I cannot provide direct answers."
            )
        }

    retrieval_results = retrieve(message)

    return {
        "response": "Here are related curriculum concepts.",
        "sources": retrieval_results["documents"][0],
    }