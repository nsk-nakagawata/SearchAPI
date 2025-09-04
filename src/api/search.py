from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal
from src.db.models import AuditLog

router = APIRouter()

@router.post("/search", response_model=SuccessResponse)
async def search(request: Request):
	api_key_auth(request)
	# ...既存の検索処理...
	response = SuccessResponse(data={"result": "dummy search result"})
	# 監査ログ保存
	db = SessionLocal()
	audit = AuditLog(
		user_id=None,  # 認証情報から取得する場合は適宜修正
		operation="search",
		request_data=str(await request.body()),
		response_data=str(response),
	)
	db.add(audit)
	db.commit()
	db.close()
	return response
# ...existing code from app/api/search.py...
