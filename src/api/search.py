from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth

router = APIRouter()

@router.post("/search")
async def search(request: Request):
	api_key_auth(request)
	# ...既存の検索処理...
	return {"result": "dummy search result"}
# ...existing code from app/api/search.py...
