from app.guardrails.rules import BLOCKED_PATTERNS


def detect_direct_answer(response: str) -> bool:
    response_lower = response.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in response_lower:
            return True

    return False

def detect_solution_leak(response: str) -> bool:

    suspicious_patterns = [
    "def ",
    "class ",
    "return ",
    "print(",
    "```",
    "the answer is",
    "the correct answer is",
    "here is the code",
    "copy and paste",
    "complete solution",
    "full solution",
    ]

    response_lower = response.lower()

    return any(
        pattern in response_lower
        for pattern in suspicious_patterns
    )