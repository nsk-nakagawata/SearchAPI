from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal
from src.db.models import AuditLog, Zairyom

router = APIRouter()

from fastapi import Body

@router.post("/update", response_model=SuccessResponse)
async def update(
	SYOCD: str = Body(...),
	HACNO: str = Body(...),
	HACREN: str = Body(...),
	embedding: list = Body(...),
	request: Request = None
):
	api_key_auth(request)
	db = SessionLocal()
	dummy = db.query(Zairyom).filter_by(SYOCD=SYOCD, HACNO=HACNO, HACREN=HACREN).first()
	if dummy:
		dummy.embedding = embedding
		db.commit()
		result = f"updated SYOCD={dummy.SYOCD}, HACNO={dummy.HACNO}, HACREN={dummy.HACREN}"
	else:
		result = "no record to update"
	response = SuccessResponse(data={"result": result})
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
