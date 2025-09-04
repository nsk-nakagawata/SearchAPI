from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal
from src.db.models import AuditLog

router = APIRouter()

@router.post("/delete", response_model=SuccessResponse)
async def delete(request: Request):
	api_key_auth(request)
	# ...既存の削除処理...
	response = SuccessResponse(data={"result": "dummy delete result"})
	db = SessionLocal()
	audit = AuditLog(
		user_id=None,
		operation="delete",
		request_data=str(await request.body()),
		response_data=str(response),
	)
	db.add(audit)
	db.commit()
	db.close()
	return response
# ...existing code from app/api/delete.py...
