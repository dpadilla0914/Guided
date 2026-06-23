from app.guardrails.rules import BLOCKED_PATTERNS


def detect_direct_answer(message: str) -> bool:
    
    message = message.lower().strip()

    for pattern in BLOCKED_PATTERNS:
        if pattern in message:
            return True

    return False

def detect_solution_leak(response: str) -> bool:

    suspicious_patterns = [
    "def ",
    "class ",
    "return ",
    "print(",
    "```",

    # Answer leakage
    "the answer is",
    "the correct answer is",
    "here is the code",
    "copy and paste",

    # Solution leakage
    "complete solution",
    "full solution",
    "working solution",
    "final solution",

    # Implementation leakage
    "final code",
    "completed code",
    "completed function",
    "full implementation",
    "completed implementation",
]

    response_lower = response.lower()

    return any(
        pattern in response_lower
        for pattern in suspicious_patterns
    )