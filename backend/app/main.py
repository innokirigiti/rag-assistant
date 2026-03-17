'''
Role: API entry point + routes (keep it thin)

Routes:

GET /health → returns a small dict with status + key config info

POST /upload → accepts UploadFile (one PDF) and calls ingestion service

POST /ask → accepts JSON body with question and calls QA service
'''

from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
import shutil

# App modules
from app.rag.embeddings import embed_pdf
from app.models import Question
from app.rag.retrieval import retrieve_top_k_chunks

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "Niko Hai Mzee"}


@app.get("/")
def greeting():
    return {"Hello from RAG assistant AI"}


@app.post("/uploadpdf")
async def upload_pdf(file: UploadFile = File(...)):

    # Define the upload directory
    UPLOAD_DIR = Path("../../data/uploads")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # Ensure it is a PDF
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}

    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename missing")

    save_path = UPLOAD_DIR / file.filename

    # Save the file
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Embed the file into the vector db using the file path
    embed_pdf(str(save_path))

    return {"status": "uploaded", "filename": file.filename, "path": str(save_path)}


# An endpoint for asking a question
# TODO: Extend to perform LLM calls of top K chunks & return LLM answer
@app.post("/question")
def create_question(data: Question):
    query = data.question
    top_k_chunks = retrieve_top_k_chunks(query=query)

    # Loop through the list of docs & generate a list of content
    chunk_content_list = []
    for chunk in top_k_chunks:
        chunk_content_list.append(chunk.page_content)

    return {
        "question": query,
        "answer": "This is a placeholder answer.",
        "top_chunks": chunk_content_list,
    }
