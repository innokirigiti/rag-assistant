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

# PDF → Page(Document) → chunks → embeddings → DB
# PDF → PyMuPDFLoader → pages → RecursiveCharacterTextSplitter → chunks → HuggingFaceEmbeddings → pgvector → PostgreSQL

def embed_pdf(file_path: str):

    # Load the pdf as a single doc from PyMuPDF 
    loader = PyMuPDFLoader(file_path, mode="single")
    doc = loader.load()
    doc_content = doc[0].page_content
    doc_metadata = doc[0].metadata

    # Take the entire pdf text & chunk it
    text_splitter = get_text_splitter()
    chunks = text_splitter.create_documents([doc_content], [doc_metadata])

    # Load the vectorstore and add the docs
    vector_store = get_vectorstore()
    vector_store.add_documents(chunks)

    return {"status":"chunks added to the db"}

