BLOCKED_PATTERNS = [

    # Direct answer requests
    "give me the answer",
    "what is the answer",
    "the exact answer",
    "just tell me",
    "final answer",
    "correct answer",

    # Homework bypass attempts
    "solve this for me",
    "do my homework",
    "do it for me",
    "complete this for me",

    # Code generation requests
    "write the code",
    "give me the code",
    "full solution",
    "complete solution",
    "working solution",
    "use this exact code",
    "copy and paste",

    # Output leakage indicators
    "the answer is",
    "here is the code",
    "use this solution",
    "the correct answer is",
]

def should_block_input(message: str) -> bool:

    message = message.lower()

    return any(
        pattern in message
        for pattern in BLOCKED_PATTERNS
    )

def contains_forbidden_output(response: str) -> bool:

    response = response.lower()

    forbidden_patterns = [
        "def ",
        "class ",
        "```",
        "final answer",
        "the answer is",
    ]

    return any(
        pattern in response
        for pattern in forbidden_patterns
    )