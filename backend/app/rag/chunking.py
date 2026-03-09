"""
Role: chunking only

Expose:

get_text_splitter()

Optional helpers:

make_metadata(filename, page=None, chunk_index=None)
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.settings import get_settings



# Using langchain RecursiveCharacterTextSplitter
# paragraph → sentence → word → character
def get_text_splitter():
    """Return a configured text splitter for RAG chunking."""
    settings = get_settings()

    return RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
    )