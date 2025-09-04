from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from src.api.response_models import ErrorResponse

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(message=exc.detail).dict()
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(message="Internal Server Error").dict()
    )
