"""
AECAgent-RAG Settings
=====================
Configuration for LLM API keys, Model parameters, and Vector Store paths.
"""

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "your-key-here")
    DEFAULT_MODEL: str = "gemini-1.5-flash"
    
    # RAG Configuration
    CHROMA_DB_PATH: str = "./data/vector_db"
    CHUNK_SIZE: int = 1500
    CHUNK_OVERLAP: int = 200
    
    # Project Info
    AGENT_VERSION: str = "1.0.0"
    AGENT_NAME: str = "AECAgent-RAG"

    class Config:
        env_file = ".env"

# Initialized settings instance
settings = Settings()
