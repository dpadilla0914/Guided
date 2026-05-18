from app.retrieval import retrieve


def process_chat(message: str):
    retrieval_results = retrieve(message)

    return {
        "response": "Here are related curriculum concepts.",
        "sources": retrieval_results["documents"][0],
    }