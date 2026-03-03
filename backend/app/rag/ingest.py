'''
Role: ingestion pipeline

Expose:

IngestionService

ingest_pdf(file_bytes: bytes, filename: str) -> dict

Return dict example (conceptually):

{"status": "ok", "filename": "...", "chunks_added": N, "collection": "active"}
'''