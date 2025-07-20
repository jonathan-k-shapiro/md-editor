"""
Markdown Document Management System - FastAPI Backend
Main application entry point.
"""

from datetime import datetime
from typing import Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

from app.core.config import settings
from app.core.logging import setup_logging

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logging()

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A collaborative web application for editing markdown documents with git integration",
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)


@app.get("/", tags=["Root"])
async def root() -> Dict[str, Any]:
    """Root endpoint providing basic API information."""
    return {
        "message": "Markdown Document Management System API",
        "version": settings.APP_VERSION,
        "status": "running",
        "docs_url": settings.DOCS_URL,
        "redoc_url": settings.REDOC_URL
    }


@app.get("/health", tags=["Health"])
async def health_check() -> Dict[str, Any]:
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/api/health", tags=["Health"])
async def api_health_check() -> Dict[str, Any]:
    """API-specific health check endpoint."""
    return {
        "status": "healthy",
        "checks": {
            "database": "not_implemented",  # TODO: Add DB check
            "redis": "not_implemented",     # TODO: Add Redis check
            "git_service": "not_implemented"  # TODO: Add Git service check
        },
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD and settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
