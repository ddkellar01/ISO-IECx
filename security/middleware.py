"""API key validation middleware for securing ISO-IECx endpoints."""
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from config.settings import settings

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in ["/health", "/docs", "/openapi.json"]:
            return await call_next(request)
            
        auth_header = request.headers.get("Authorization")
        if not auth_header or auth_header != f"Bearer {settings.API_KEY_SECRET}":
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or missing API key authorization."}
            )
            
        return await call_next(request)
