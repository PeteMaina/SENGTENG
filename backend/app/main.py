"""
Senteng Fashions Backend - Main Application Entry Point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os

from app.core.config import settings
from app.api.v1.router import api_router

# Create FastAPI app instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Senteng Fashions E-Commerce Platform API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory if it doesn't exist
os.makedirs("uploads", exist_ok=True)

# Mount static files for uploads
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint - API health check
    """
    return JSONResponse(
        content={
            "message": "Welcome to Senteng Fashions API",
            "version": "1.0.0",
            "docs": "/docs",
            "health": "healthy"
        }
    )


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for monitoring
    """
    return JSONResponse(
        content={
            "status": "healthy",
            "environment": settings.ENVIRONMENT
        }
    )


# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Actions to perform on application startup
    """
    print("🚀 Senteng Fashions Backend starting up...")
    print(f"📝 Environment: {settings.ENVIRONMENT}")
    print(f"📚 API Docs available at: /docs")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform on application shutdown
    """
    print("👋 Senteng Fashions Backend shutting down...")
