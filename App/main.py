
from importlib import import_module
from pathlib import Path
import sys

from fastapi import FastAPI

# Make the project root importable when this file is run directly or through uvicorn.
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

users_router = import_module("aritaro.api.routes.users").router

app = FastAPI(
    title="ARITARO-SEO-INTELLIGENCE",
    description="Backend API for ARITARO-SEO-INTELLIGENCE platform.",
    version="1.0.0"
)

# Register API routes
app.include_router(users_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to ARITARO-SEO-INTELLIGENCE API!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API is running smoothly."
    }

