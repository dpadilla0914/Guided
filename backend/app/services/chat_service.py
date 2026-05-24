from app.retrieval import retrieve
from app.guardrails.detector import (
    detect_direct_answer,
    detect_solution_leak,
)

from app.services.llm_service import generate_response


def process_chat(message: str):

    # INPUT GUARDRAIL
    if detect_direct_answer(message):
        return {
            "response": (
                "I can help guide you through concepts, "
                "but I cannot provide direct answers."
            )
        }

    # RETRIEVAL
    try:

        retrieval_results = retrieve(message)

    except Exception as e:

        print("RETRIEVAL ERROR:", e)

        return {
            "response": (
                "I'm having trouble accessing the curriculum "
                "database right now."
            )
        }
    
    # LIMIT CONTEXT
    top_chunks = retrieval_results["documents"][0][:2]

    context = "\n\n".join(top_chunks)

    # LLM GENERATION
    llm_response = generate_response(
        question=message,
        context=context,
    )

    # OUTPUT GUARDRAIL
    if detect_solution_leak(llm_response):
        llm_response = (
            "Let's focus on understanding concepts "
            "instead of direct answers."
        )

    return {
        "response": llm_response,
        "sources": top_chunks,
    }