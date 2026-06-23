STRUGGLE_PATTERNS = [
    "i'm stuck",
    "im stuck",
    "i don't understand",
    "i dont understand",
    "i'm confused",
    "im confused",
    "i'm lost",
    "im lost",
    "nothing works",
    "i've tried",
    "ive tried",
    "help me",
]


def detect_struggle(message: str) -> bool:

    message = message.lower()

    return any(
        pattern in message
        for pattern in STRUGGLE_PATTERNS
    )