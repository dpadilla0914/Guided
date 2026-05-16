from backend.app.guardrails.detector import detect_direct_answer
from backend.app.guardrails.rewrite import rewrite_response


def apply_guardrails(student_question: str, model_response: str):
    flagged = detect_direct_answer(model_response)

    if flagged:
        return {
            "guardrail_triggered": True,
            "final_response": rewrite_response(student_question),
        }

    return {
        "guardrail_triggered": False,
        "final_response": model_response,
    }


student_question = "How do I use OpenAPI to build a weather app?"

unsafe_model_response = """
Here is the code for your FastAPI weather endpoint.
Use this exact code and copy and paste it into your app.
"""

safe_model_response = """
Let's break this down. What input should your weather app take from the user?
"""


print("Unsafe response test:")
print(apply_guardrails(student_question, unsafe_model_response))

print("\nSafe response test:")
print(apply_guardrails(student_question, safe_model_response))
