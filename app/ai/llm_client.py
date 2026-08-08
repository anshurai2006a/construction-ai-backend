def generate_answer(question: str, context_chunks: list[dict]) -> str:
    """
    MOCK: real version sends `question` + `context_chunks` to an LLM
    (OpenAI, Claude API, etc.) and returns the generated answer.
    """
    if not context_chunks:
        return f"(Mock answer) I couldn't find relevant document context for: '{question}'"
    return f"(Mock answer) Based on the uploaded documents, here's guidance for: '{question}'"