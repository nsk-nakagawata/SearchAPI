from fastapi import APIRouter, Request
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal
from src.db.models import AuditLog, Zairyom

router = APIRouter()

from fastapi import Body

@router.post("/add", response_model=SuccessResponse)
async def add(
	SYOCD: str = Body(...),
	HACNO: str = Body(...),
	HACREN: str = Body(...),
	embedding: list = Body(...),
	request: Request = None
):
	api_key_auth(request)
	db = SessionLocal()
	dummy = Zairyom(SYOCD=SYOCD, HACNO=HACNO, HACREN=HACREN, embedding=embedding)
	db.add(dummy)
	db.commit()
	response = SuccessResponse(data={"result": f"added SYOCD={dummy.SYOCD}, HACNO={dummy.HACNO}, HACREN={dummy.HACREN}"})
	audit = AuditLog(
		user_id=None,
		operation="add",
		request_data=str(await request.body()),
		response_data=str(response),
	)
	db.add(audit)
	db.commit()
	db.close()
	return response
# ...existing code from app/api/add.py...
