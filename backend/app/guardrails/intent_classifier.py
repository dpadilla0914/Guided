def classify_intent(message: str) -> str:

    message = message.lower()

    if any(
        phrase in message
        for phrase in [
            "give me the answer",
            "write the code",
            "solve this",
        ]
    ):
        return "ANSWER_REQUEST"

    if any(
        phrase in message
        for phrase in [
            "debug",
            "error",
            "exception",
            "not working",
        ]
    ):
        return "DEBUGGING"

    if any(
        phrase in message
        for phrase in [
            "build",
            "project",
            "app",
        ]
    ):
        return "PROJECT"

    return "EXPLANATION"