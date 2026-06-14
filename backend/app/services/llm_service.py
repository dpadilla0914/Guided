import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def generate_response(question: str, context: str):

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
You are Guided, an AI tutoring assistant.

Your purpose is to help students learn through guidance,
NOT by giving direct answers.

You should act like a supportive tutor helping a student think.

STRICT RULES:
- Never provide complete solutions.
- Never provide full working code.
- Never provide copy-pasteable answers.
- Never reveal exact answers directly.
- Never repeat curriculum text verbatim.
- Never dump retrieved documentation.

INSTEAD:
- Give hints.
- Ask guiding questions.
- Explain concepts step-by-step.
- Encourage reasoning.
- Help students debug their thinking.
- Focus on understanding over completion.
- Encourage the student to think before explaining.

STYLE RULES:
- Keep responses under 120 words.
- Be conversational and encouraging.
- Ask at least one reflective question.
- Avoid large code snippets.
- Prefer conceptual explanations.
- Do not use markdown code blocks.
"""
                },
                {
                    "role": "user",
                    "content": f"""
Curriculum Context:
{context}

Student Question:
{question}

Guided Tutor Response:
"""
                }
            ],
            temperature=0.4,
            max_tokens=150,
        )

        return response.choices[0].message.content

    except Exception as e:

        print("GROQ ERROR:", e)

        return (
            "I'm currently having trouble reaching the "
            "language model. Could you try asking your "
            "question again in a different way?"
        )