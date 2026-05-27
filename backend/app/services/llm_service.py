import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


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

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:

        print("GROQ ERROR:", e)

        return (
            "I'm currently having trouble reaching the "
            "language model, but I can still help guide "
            "you using retrieved curriculum concepts."
        )