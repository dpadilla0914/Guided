from app.retrieval import retrieve
from app.guardrails.detector import (
    detect_direct_answer,
    detect_solution_leak,
)
from app.services.profile_service import (
    add_message,
    get_recent_history,
    load_profile,
)
from app.services.llm_service import generate_response
from app.guardrails.intent_classifier import (
    classify_intent,
)
from app.guardrails.struggle_detector import (
    detect_struggle,
)


def process_chat(message: str, student_id: str,):

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
    metadata = retrieval_results.get("metadatas", [[]])[0]

    topic = None

    if metadata:
        topic = metadata[0].get("source")

    if not documents:

        return {
            "response": (
                "I couldn't find enough curriculum context "
                "to answer that confidently.\n\n"
                "Could you rephrase the question or be more specific?"
            )
        }

    top_chunks = documents[:1]

    context = "\n\n".join(
        chunk[:150]
        for chunk in top_chunks
    )

    # LLM GENERATION
    intent = classify_intent(message)

    struggling = detect_struggle(message)
        
    profile = load_profile(student_id)

    history = get_recent_history(
        student_id=student_id,
    )

    llm_response = generate_response(
        question=message,
        context=context,
        intent=intent,
        struggling=struggling,
        history=history,
        profile=profile,
    )

    llm_response = llm_response.strip()

    add_message(
        student_id,
        "user",
        message,
    )

    add_message(
        student_id,
        "assistant",
        llm_response,
    )

    # OUTPUT GUARDRAIL
    if detect_solution_leak(llm_response):

        guardrail_response = (
            "Let's focus on understanding the concept instead of jumping to a solution. "
            "What part of the problem feels most confusing right now?"
        )

        add_message(
            student_id,
            "assistant",
            guardrail_response,
        )

        return {
            "response": guardrail_response,
            "intent": intent,
            "struggling": struggling,
            "topic": topic,
        }

    return {
        "response": llm_response,
        "intent": intent,
        "struggling": struggling,
        "topic": topic,
    }