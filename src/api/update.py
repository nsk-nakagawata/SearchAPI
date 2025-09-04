from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse

router = APIRouter()

@router.post("/update", response_model=SuccessResponse)
async def update(request: Request):
	api_key_auth(request)
	# ...既存の更新処理...
	return SuccessResponse(data={"result": "dummy update result"})
# ...existing code from app/api/update.py...
