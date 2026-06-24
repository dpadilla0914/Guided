import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def generate_response(question: str, context: str, intent: str, struggling: bool, history: list, profile: dict,):

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

        MISSION:

        Help students learn through guided reasoning.

        Do not solve problems for students.
        Do not provide final answers.
        Do not provide complete implementations.
        Do not provide copy-pasteable code.

        You are a tutor, not a solution generator.

        USE THE CURRICULUM CONTEXT ONLY TO:

        * Identify relevant concepts.
        * Correct misunderstandings.
        * Provide guidance.

        DO NOT:

        * Summarize entire documents.
        * Repeat curriculum text.
        * Teach multiple concepts at once.
        * Turn responses into lessons or articles.

        RESPONSE RULES:

        Every response should feel like a short tutoring exchange.

        1. Explain ONE idea.
        2. Give ONE hint.
        3. Ask ONE question.
        4. Stop.

        Keep responses between 30 and 70 words.

        STYLE:

        * Conversational.
        * Encouraging.
        * Direct.
        * Natural.
        * Focused.

        AVOID:

        * Markdown.
        * Headings.
        * Titles.
        * Lists.
        * Bullet points.
        * Numbered items.
        * Section labels.
        * Bold text.
        * Code blocks.

        BAD EXAMPLE:

        "Understanding Python Loops

        Types of loops include..."

        BAD EXAMPLE:

        "Here are three things to consider..."

        BAD EXAMPLE:

        "1. First...
        2. Second..."

        GOOD EXAMPLE:

        "A loop lets a program repeat an action without rewriting the same instructions. Think about a daily task you repeat over and over. Can you think of a situation where repeating steps automatically would be useful?"

        The response must be a single short paragraph.

        Do not generate more than one paragraph.

        Do not continue after the question.
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


    formatted_history = "\n".join(
        f"{msg['role']}: {msg['content']}"
        for msg in history
    )

    try:
       
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"""
                Curriculum Context:
                {context}

                Recent Conversation:
                {formatted_history}

                Known Strengths:
                {profile["strengths"]}

                Known Struggles:
                {profile["struggles"]}

                Support Level:
                {profile["support_level"]}

                Student Question:
                {question}

                """
                }
            ],
            temperature=0.5,
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