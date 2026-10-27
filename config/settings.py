"""Global application configuration management using Pydantic Settings."""
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "ISO-IECx"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CHROMA_HOST: str = os.getenv("CHROMA_HOST", "localhost")
    CHROMA_PORT: int = int(os.getenv("CHROMA_PORT", "8000"))
    API_KEY_SECRET: str = os.getenv("API_KEY_SECRET", "default-dev-secret")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
