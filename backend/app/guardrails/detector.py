from backend.app.guardrails.rules import BLOCKED_PATTERNS


def detect_direct_answer(response: str) -> bool:
    response_lower = response.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in response_lower:
            return True

    return False
