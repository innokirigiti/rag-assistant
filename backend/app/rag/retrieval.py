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
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

settings = get_settings()

# This function retrieves top K chunks from the vectorDB based on similarity to the search query
# The return type is a list of langchain documents
def retrieve_top_k_chunks(query: str) -> list:
    vector_store = get_vectorstore()

    return vector_store.similarity_search(query=query, k = settings.TOP_K)

def generate_llm_answer(query: str) -> str:
    """Takes in a user query and returns an llm generated answer"""

    ## Define an llm instance
    llm = ChatOpenAI(model=settings.OPENAI_CHAT_MODEL, temperature=0)

    ## Define the prompt temptate
    prompt_template = """
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
        """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # Generate context from retrieved top k chunks
    chunks = retrieve_top_k_chunks(query)
    context = "\n\n".join(chunk.page_content for chunk in chunks)

    # Define a chain
    rag_chain = prompt | llm | StrOutputParser()

    return rag_chain.invoke({"question": query, "context": context})
