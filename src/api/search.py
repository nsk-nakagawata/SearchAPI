from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse

router = APIRouter()

@router.post("/search", response_model=SuccessResponse)
async def search(request: Request):
	api_key_auth(request)
	# ...既存の検索処理...
	return SuccessResponse(data={"result": "dummy search result"})
# ...existing code from app/api/search.py...
