from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth

router = APIRouter()

@router.post("/delete")
async def delete(request: Request):
	api_key_auth(request)
	# ...既存の削除処理...
	return {"result": "dummy delete result"}
# ...existing code from app/api/delete.py...
