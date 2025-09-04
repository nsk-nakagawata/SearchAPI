from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse

router = APIRouter()

@router.post("/delete", response_model=SuccessResponse)
async def delete(request: Request):
	api_key_auth(request)
	# ...既存の削除処理...
	return SuccessResponse(data={"result": "dummy delete result"})
# ...existing code from app/api/delete.py...
