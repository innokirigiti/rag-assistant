'''
Role: ingestion pipeline

Expose:

IngestionService

embed_pdf(file_path: str): -> dict

Return dict example (conceptually):

{"status": "ok", "filename": "...", "chunks_added": N, "collection": "active"}
'''
from langchain_community.document_loaders import PyMuPDFLoader
from app.rag.chunking import get_text_splitter
from app.rag.vectorstore import get_vectorstore

# PDF → chunks → embeddings → DB

def embed_pdf(file_path: str):

    # Load the pdf as a single doc from PyMuPDF 
    loader = PyMuPDFLoader(file_path, mode="single")
    docs = loader.load()

    # Load the vectorstore and add the docs
    vector_store = get_vectorstore()
    vector_store.add_documents(docs)

    return {"status":"added", }