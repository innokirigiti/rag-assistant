# 🧠  DocAI - an AI Agent assistant for documents

**FastAPI + Streamlit + pgvector + OpenAI**

------------------------------------------------------------------------

## 📌 Project Overview

This project implements a **containerized Retrieval-Augmented Generation
(RAG) system** for interacting with documents.

Users can:

-   Upload PDF documents\
-   Index them into a vector database\
-   Ask questions in natural language\
-   Receive grounded answers with citations (document name + page +
    snippet)

The system is built with a clean separation of concerns:

-   **FastAPI** → Backend AI service layer\
-   **Streamlit** → User interface\
-   **Postgres + pgvector** → Vector storage\
-   **SQLAlchemy** → ORM and database control\
-   **OpenAI API** → Embeddings + LLM generation\
-   **Docker Compose** → Fully containerized local environment

------------------------------------------------------------------------

## 🏗 Architecture Overview

High-level flow:

    Streamlit UI
          ↓
    FastAPI Backend
          ↓
    LangChain (Embeddings + LLM)
          ↓
    Postgres + pgvector

### Ingestion Pipeline

    PDF → Text Extraction → Cleaning → Chunking → Embeddings → Database

### Query Pipeline

    User Question
        ↓
    Embed Question
        ↓
    Vector Similarity Search (pgvector)
        ↓
    Build Prompt (Context + Question)
        ↓
    LLM Generates Grounded Answer
        ↓
    Return Answer + Citations

------------------------------------------------------------------------

## 📂 Project Structure

    rag-assistant/
    │
    ├── backend/
    │   ├── app/
    │   │   ├── main.py              # FastAPI entry point
    │   │   └── rag/
    │   │       ├── ingest.py        # PDF → chunk → embed → store
    │   │       ├── qa.py            # Retrieval + LLM answer logic
    │   │       ├── db.py            # SQLAlchemy engine/session
    │   │       ├── models.py        # ORM models (documents, chunks)
    │   │       └── settings.py      # Configuration (env variables)
    │   │
    │   ├── requirements.txt         # Backend dependencies
    │   └── Dockerfile               # Backend container
    │
    ├── ui/
    │   ├── app.py                   # Streamlit interface
    │   ├── requirements.txt         # UI dependencies
    │   └── Dockerfile               # UI container
    │
    ├── docker-compose.yml           # Local multi-container setup
    ├── .env                         # Environment variables
    └── data/uploads/                # Local PDF storage (dev)

------------------------------------------------------------------------

## 🔹 Component Responsibilities

### 🖥 Streamlit (Frontend)

-   Upload PDFs
-   Trigger ingestion
-   Send questions to backend
-   Display answers + sources
-   Maintain chat history

Streamlit does **not** handle:

-   Embeddings
-   Database access
-   LLM calls

------------------------------------------------------------------------

### ⚙ FastAPI (Backend AI Service)

-   `/ingest` endpoint
-   `/ask` endpoint
-   Text extraction (PyMuPDF)
-   Chunking logic
-   Embedding generation (OpenAI)
-   Vector similarity search
-   Prompt construction
-   Citation formatting

All RAG logic lives here.

------------------------------------------------------------------------

### 🗄 Postgres + pgvector

Stores:

-   Document metadata
-   Text chunks
-   Embedding vectors
-   Page numbers
-   Optional JSON metadata

Vector similarity search uses:

``` sql
ORDER BY embedding <-> :query_vector
LIMIT k;
```

------------------------------------------------------------------------

### 🤖 OpenAI

Used for:

-   Text embeddings (indexing + query)
-   Chat model (final grounded answer)

------------------------------------------------------------------------

## 🚀 Running Locally

### 1️⃣ Set Environment Variables

Create `.env` file:

    OPENAI_API_KEY=your_key_here
    DATABASE_URL=postgresql+psycopg://user:password@db:5432/ragdb
    OPENAI_EMBED_MODEL=text-embedding-3-large
    OPENAI_CHAT_MODEL=gpt-4o-mini
    API_BASE_URL=http://api:8000

------------------------------------------------------------------------

### 2️⃣ Build and Run

    docker compose up --build

Access:

-   UI → http://localhost:8501\
-   API docs → http://localhost:8000/docs

------------------------------------------------------------------------

## ✅ MVP Completion Criteria

-   Containers start successfully\
-   PDFs upload and ingest correctly\
-   Embeddings are stored in Postgres\
-   Questions return grounded answers\
-   Citations include document + page number

------------------------------------------------------------------------

## 🎯 Future Extensions

-   Add LangGraph agent loop (retrieve → draft → critique → retry)\
-   Add metadata filtering (department/date)\
-   Move document storage to S3\
-   Deploy to AWS ECS + RDS\
-   Add authentication and role-based filtering

------------------------------------------------------------------------

## 🧠 Design Philosophy

-   Clean separation of UI and AI logic\
-   SQLAlchemy for explicit database control\
-   pgvector for transparent similarity search\
-   Container-first development\
-   Production-aligned architecture
