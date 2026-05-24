import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(question: str, context: str):

    prompt = f"""
You are Guided, an AI learning assistant.

You help students learn concepts through:
- hints
- guided explanations
- Socratic questioning

You NEVER:
- provide complete solutions
- provide copy-paste answers
- do assignments for students

Use the curriculum context below to answer the student's question.

Curriculum Context:
{context}

Student Question:
{question}

Instructions:
- Keep responses under 150 words
- Be conversational
- Explain concepts clearly
- Ask at least one guiding question
- Do not dump raw curriculum text
- Avoid long code blocks
- Focus on understanding, not answers
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False,
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60,
        )

        result = response.json()

        return result["response"]

    except Exception as e:

        print("OLLAMA ERROR:", e)

        return (
            "I'm currently unable to reach the language model, "
            "but I can still help guide you using retrieved concepts."
        )