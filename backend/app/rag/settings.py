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
    # OpenAI
    # -----------------------------
    OPENAI_API_KEY: str
    OPENAI_EMBED_MODEL: str
    OPENAI_CHAT_MODEL: str

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str

    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None

    # -----------------------------
    # UI
    # -----------------------------
    API_BASE_URL: str | None = None

    # -----------------------------
    # RAG Configuration (Defaults)
    # -----------------------------
    COLLECTION_NAME: str = "active"
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 150
    TOP_K: int = 6

    # Optional: useful for enforcing embedding dimension
    EMBEDDING_DIM: int = 3072  # text-embedding-3-large default

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

