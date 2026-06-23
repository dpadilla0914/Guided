def get_tutoring_mode(
    intent,
    struggling=False,
):
    if struggling:
        return "supportive"

    if intent == "debugging":
        return "debug"

    return "standard"