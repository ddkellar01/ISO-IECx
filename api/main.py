"""FastAPI application entry point for the ISO-IECx core service."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router
from security.middleware import APIKeyMiddleware

app = FastAPI(
    title="ISO-IECx Intelligence & Google Flow Engine",
    version="1.0.0",
    description="Autonomous ISO/IEC compliance intelligence and video generation orchestration."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(APIKeyMiddleware)
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ISO-IECx Core"}
