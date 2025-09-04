from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal
from src.db.models import AuditLog

router = APIRouter()

@router.post("/update", response_model=SuccessResponse)
async def update(request: Request):
	api_key_auth(request)
	# ...既存の更新処理...
	response = SuccessResponse(data={"result": "dummy update result"})
	db = SessionLocal()
	audit = AuditLog(
		user_id=None,
		operation="update",
		request_data=str(await request.body()),
		response_data=str(response),
	)
	db.add(audit)
	db.commit()
	db.close()
	return response
# ...existing code from app/api/update.py...
