from fastapi import APIRouter, Request
from typing import List
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal
from src.db.models import AuditLog, Zairyom

router = APIRouter()

from fastapi import Body

@router.post("/search", response_model=SuccessResponse)
async def search(
	request: Request,
	embedding: List[float] = Body(...)
):
	api_key_auth(request)
	db = SessionLocal()
	# 実際はembeddingベクトルで近傍検索するが、ここでは全件返却例
	dummy_result = db.query(Zairyom).limit(5).all()
	response = SuccessResponse(data={"result": [f"SYOCD={r.SYOCD}, HACNO={r.HACNO}, HACREN={r.HACREN}" for r in dummy_result]})
	audit = AuditLog(
		user_id=None,
		operation="search",
		request_data=str(await request.body()),
		response_data=str(response),
	)
	db.add(audit)
	db.commit()
	db.close()
	return response
# ...existing code from app/api/search.py...
