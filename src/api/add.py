from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth

router = APIRouter()

@router.post("/add")
async def add(request: Request):
	api_key_auth(request)
	# ...既存の追加処理...
	return {"result": "dummy add result"}
# ...existing code from app/api/add.py...
