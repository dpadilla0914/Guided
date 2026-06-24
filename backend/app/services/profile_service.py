import json

from pathlib import Path


PROFILE_DIR = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
    / "data"
    / "student_profiles"
)

PROFILE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def load_profile(student_id: str):

    profile_path = PROFILE_DIR / f"{student_id}.json"

    if not profile_path.exists():

        return {
            "student_id": student_id,
            "strengths": [],
            "struggles": [],
            "topics_seen": [],
            "support_level": "normal",
            "history": [],
        }

    with open(profile_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_profile(profile: dict):

    profile_path = (
        PROFILE_DIR /
        f"{profile['student_id']}.json"
    )

    with open(profile_path, "w", encoding="utf-8") as file:
        json.dump(
            profile,
            file,
            indent=2,
        )

def add_message(
    student_id: str,
    role: str,
    content: str,
):

    profile = load_profile(student_id)

    profile["history"].append(
        {
            "role": role,
            "content": content,
        }
    )

    profile["history"] = (
        profile["history"][-10:]
    )

    save_profile(profile)


def get_recent_history(
    student_id: str,
    limit: int = 6,
):

    profile = load_profile(student_id)

    return profile["history"][-limit:]