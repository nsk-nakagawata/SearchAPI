from pydantic import BaseModel
from typing import Any, Optional

class SuccessResponse(BaseModel):
    status: str = "success"
    data: Optional[Any]

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
