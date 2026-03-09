# A script to test if things workout

"""
Simple end-to-end test for:

- HuggingFace embeddings
- PostgreSQL + pgvector
- LangChain PGVector
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from langchain_core.documents import Document
import psycopg

# -----------------------------
# Configuration
# -----------------------------

DATABASE_URL = "postgresql+psycopg://raguser:ragpassword@localhost:5432/ragdb"
COLLECTION_NAME = "demo_docs"

# -----------------------------
# Step 1: Initialize embeddings
# -----------------------------

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# quick test
vec = embeddings.embed_query("hello world")
print("Embedding dimension:", len(vec))


# -----------------------------
# Step 2: Create vector store
# -----------------------------

print("Connecting to pgvector...")

vector_store = PGVector(
    embeddings=embeddings,
    connection=DATABASE_URL,
    collection_name=COLLECTION_NAME,
    use_jsonb=True,
)

print("Vector store ready")


# -----------------------------
# Step 3: Create sample docs
# -----------------------------

docs = [
    Document(page_content="Cats like to sleep in the sun."),
    Document(page_content="Dogs are loyal animals."),
    Document(page_content="Apples and oranges are fruits."),
    Document(page_content="Human also like sun")
]

print("Adding documents to vector store...")

vector_store.add_documents(docs)

print("Documents inserted.")


# -----------------------------
# Step 4: Similarity search
# -----------------------------

query = "Which animals like sunshine?"

print("\nQuery:", query)

results = vector_store.similarity_search(query, k=2)

print("\nTop results:")

for r in results:
    print("-", r.page_content)


print("\nDemo finished successfully.")