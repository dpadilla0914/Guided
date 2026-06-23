BLOCKED_PATTERNS = [

    # Direct answer requests
    "give me the answer",
    "what is the answer",
    "the exact answer",
    "just tell me",
    "final answer",
    "correct answer",
    "show me the answer",
    "answer this for me",

    # Homework bypass attempts
    "solve this for me",
    "solve it for me",
    "solve this",
    "solve it",
    "do my homework",
    "do it for me",
    "complete this for me",

    # Solution requests
    "sample answer",
    "example answer",
    "show me the solution",
    "provide a solution",
    "working solution",
    "complete solution",
    "full solution",
    "correct solution",

    # Implementation requests
    "generate the implementation",
    "final implementation",
    "complete implementation",
    "completed implementation",
    "finished implementation",
    "show me the completed project",
    "show me the finished version",
    "give me the finished version",

    # Code generation requests
    "write the code",
    "give me the code",
    "provide the code",
    "show me the code",
    "generate the code",
    "full code",
    "final code",
    "completed function",
    "provide a working example",
    "working example",

    # Copy-paste attempts
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