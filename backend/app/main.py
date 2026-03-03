'''
Role: API entry point + routes (keep it thin)

Routes:

GET /health → returns a small dict with status + key config info

POST /upload → accepts UploadFile (one PDF) and calls ingestion service

POST /ask → accepts JSON body with question and calls QA service
'''

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def greeting():
    return {"Hello from RAG assistant AI"} 