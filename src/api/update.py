from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth

router = APIRouter()

@router.post("/update")
async def update(request: Request):
	api_key_auth(request)
	# ...既存の更新処理...
	return {"result": "dummy update result"}
# ...existing code from app/api/update.py...
