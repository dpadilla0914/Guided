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

        distances = retrieval_results.get("distances", [[]])[0]

        if distances and distances[0] > 1.2:

            return {
                "response": (
                    "I'm not confident I found the right curriculum "
                    "context for that question.\n\n"
                    "Could you rephrase it or provide more detail?"
                )
            }

    except Exception as e:

        print("RETRIEVAL ERROR:", e)

        return {
            "response": (
                "I'm having trouble accessing the curriculum "
                "database right now."
            )
        }
    
    # LIMIT CONTEXT
    documents = retrieval_results.get("documents", [[]])[0]

    if not documents:

        return {
            "response": (
                "I couldn't find enough curriculum context "
                "to answer that confidently.\n\n"
                "Could you rephrase the question or be more specific?"
            )
        }
    top_chunks = documents[:2]

    context = "\n\n".join(
    chunk[:150]
    for chunk in top_chunks

    )

    # LLM GENERATION
    llm_response = generate_response(
        question=message,
        context=context,
    )

    llm_response = llm_response.strip()

    # OUTPUT GUARDRAIL
    if detect_solution_leak(llm_response):
        llm_response = (
            "I want to help you reason through the problem "
            "instead of giving a direct solution.\n\n"
            "What part feels most confusing right now?"
        )

    return {
        "response": llm_response,
    }