'''
Role: retrieval + LLM answer

Expose:

QAService

answer(question: str, top_k: int | None = None) -> dict

Return dict example:

{"answer": "...", "sources": [...], "used_top_k": k}

(Maybe I can keep sources as a list of dicts extracted from metadata.)
'''