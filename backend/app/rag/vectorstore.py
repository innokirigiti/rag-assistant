'''
Role: one place for PGVector wiring

Expose:

get_embeddings()

get_vectorstore()

reset_collection() (single document rule)

get_retriever(k=None, search_type="similarity", filters=None)
'''
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from app.rag.settings import get_settings

settings = get_settings()


connection = settings.DATABASE_URL  # Uses psycopg3!
collection_name = settings.COLLECTION_NAME

# Define a vector store using Postgress + pgvector


# Expose the embeddings
def get_embeddings():
    return OpenAIEmbeddings(model=settings.OPENAI_EMBED_MODEL)

# Expose the vector_store
def get_vectorstore():
        embeddings = get_embeddings()
        
        return PGVector(embeddings=embeddings,
        collection_name=collection_name,
        connection=connection,
        use_jsonb=True,)