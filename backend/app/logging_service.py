import json
from datetime import datetime, timezone
from pathlib import Path


LOG_FILE = Path("data/chat_logs.jsonl")


def log_interaction(
    user_input: str,
    system_output: str,
    intent: str = None,
    struggling: bool = False,
    topic: str = None,
    guardrail_triggered: str = None,
):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_input": user_input,
        "system_output": system_output,

        # Analytics
        "intent": intent,
        "struggling": struggling,
        "topic": topic,
        "guardrail_triggered": guardrail_triggered,
    }

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(log_entry) + "\n")

    return log_entry


def get_logs():
    if not LOG_FILE.exists():
        return []

    logs = []

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            logs.append(json.loads(line))

    return logs