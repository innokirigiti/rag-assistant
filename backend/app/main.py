'''
Role: API entry point + routes (keep it thin)

Routes:

GET /health → returns a small dict with status + key config info

POST /upload → accepts UploadFile (one PDF) and calls ingestion service

POST /ask → accepts JSON body with question and calls QA service
'''

from fastapi import FastAPI
from app.rag.embeddings import embed_pdf

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "Niko Hai Mzee"}


@app.get("/")
def greeting():
    return {"Hello from RAG assistant AI"} 

# TODO: update to accept a pdf file path from the UI later
@app.get("/embed")
def embed():
    # Hard coded test file path
    path = "../../data/uploads/test.pdf"
    return embed_pdf(path)