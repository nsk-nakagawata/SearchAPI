from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse

router = APIRouter()

@router.post("/add", response_model=SuccessResponse)
async def add(request: Request):
	api_key_auth(request)
	# ...既存の追加処理...
	return SuccessResponse(data={"result": "dummy add result"})
# ...existing code from app/api/add.py...
