import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def generate_response(question: str, context: str, intent: str, struggling: bool):

    tutoring_mode = "standard"

    if struggling:
        tutoring_mode = "supportive"

    if intent == "DEBUGGING":
        tutoring_mode = "debugging"

    if intent == "PROJECT":
        tutoring_mode = "project"

    system_prompt = f"""
    You are Guided, an AI tutoring assistant.

    Current tutoring mode: {tutoring_mode}

    Your purpose is to help students learn through guidance,
    NOT by giving direct answers.

    STRICT RULES:
    - Never provide complete solutions.
    - Never provide full working code.
    - Never provide copy-pasteable answers.
    - Never reveal exact answers directly.
    - Never repeat curriculum text verbatim.
    - Never dump retrieved documentation.

    TUTORING RULES:
    - Keep responses under 80 words.
    - Focus on ONE concept at a time.
    - Give only ONE next step.
    - Ask EXACTLY ONE guiding question.
    - Do not ask multiple questions.
    - Do not list multiple next steps.
    - Do not overwhelm the student.
    - Avoid repeating previous guidance.

    RESPONSE FORMAT:

    - Give a short explanation (1-2 sentences).
    - Give one helpful hint.
    - Ask exactly one guiding question.
    - Keep the response under 80 words.
    - Make the response feel natural and conversational.
    - Do NOT use labels such as Concept, Hint, or Question.
    - Do NOT use bullet points.
    - Do NOT use numbered lists.
    - Respond as a tutor speaking directly to a student.
    """

    if tutoring_mode == "supportive":

        system_prompt += """

        The student appears confused or stuck.

        Reduce complexity.
        Do NOT introduce new concepts.
        Do NOT mention advanced terminology.
        Use a simpler explanation than normal.
        Focus on one small idea.
        Build confidence before teaching.
        Ask a question about the current concept only.
    """

    if tutoring_mode == "debugging":

        system_prompt += """

        The student is debugging.

        Do NOT suggest the likely bug.
        Do NOT provide a fix.
        Help the student gather information.
        Ask questions that narrow the search space.
        Act like a senior engineer coaching someone through debugging.
    """
        
    if tutoring_mode == "project":

        system_prompt += """

        The student is building a project.

        Focus ONLY on the next milestone.

        Do not plan the entire project.
        Do not give a complete implementation.
        Ask one question about the next step.
        """

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                "role": "system",
                "content": system_prompt,
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
            max_tokens=100,
        )

        return response.choices[0].message.content

    except Exception as e:

        print("GROQ ERROR:", e)

        return (
            "I'm currently having trouble reaching the "
            "language model. Could you try asking your "
            "question again in a different way?"
        )