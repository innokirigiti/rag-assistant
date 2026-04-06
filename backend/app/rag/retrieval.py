'''
Role: retrieval + LLM answer

Expose:

QAService

answer(question: str) -> dict

Return dict example:

{"answer": "...", "sources": [...]}

(Maybe I can keep sources as a list of dicts extracted from metadata.)
'''

from app.rag.vectorstore import get_vectorstore
from app.rag.settings import get_settings

settings = get_settings()

# This function retrieves top K chunks from the vectorDB based on similarity to the search query
# The return type is a list of langchain documents
def retrieve_top_k_chunks(query: str):
    vector_store = get_vectorstore()

    return vector_store.similarity_search(query=query, k = settings.TOP_K)

def generate_llm_answer(query: str) -> dict:
    """Takes in a user query and returns an llm generated answer"""

    # Generate the context from the query (top k chunks)
    context = retrieve_top_k_chunks(query)

    return {"answer": "LLM answer placeholder", }