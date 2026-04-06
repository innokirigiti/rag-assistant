from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

'''
Role: expose .env values 

Settings
eg. usecase:

from app.rag.settings import get_settings

settings = get_settings()
settings.OPENAI_API_KEY
'''


class Settings(BaseSettings):

    # -----------------------------
    # Embeddings
    # -----------------------------
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    EMBEDDING_DIM: int = 384

    # -----------------------------
    # LLM
    # -----------------------------
    OPENAI_CHAT_MODEL:str

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str

    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None

    # -----------------------------
    # API
    # -----------------------------
    API_BASE_URL: str | None = None

    # -----------------------------
    # RAG Configuration
    # -----------------------------
    COLLECTION_NAME: str = "my_docs"
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 150
    TOP_K: int = 6

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()