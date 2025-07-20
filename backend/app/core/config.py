"""
Configuration management for the Markdown Document Management System.
"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application Configuration
    APP_NAME: str = Field(default="Markdown Document Management System")
    APP_VERSION: str = Field(default="0.1.0")
    DEBUG: bool = Field(default=True)
    SECRET_KEY: str = Field(default="dev-secret-key-change-in-production")
    ENVIRONMENT: str = Field(default="development")
    
    # Server Configuration
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)
    RELOAD: bool = Field(default=True)
    
    # Database Configuration
    DATABASE_URL: str = Field(default="postgresql://user:password@localhost:5432/mdeditor")
    
    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = Field(default=["http://localhost:3000", "http://127.0.0.1:3000"])
    ALLOWED_METHODS: List[str] = Field(default=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    ALLOWED_HEADERS: List[str] = Field(default=["*"])
    
    # Logging Configuration
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FORMAT: str = Field(default="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    # API Documentation
    DOCS_URL: str = Field(default="/docs")
    REDOC_URL: str = Field(default="/redoc")
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "allow"
    }


# Create global settings instance
settings = Settings()
