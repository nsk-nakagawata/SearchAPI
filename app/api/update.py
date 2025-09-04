from fastapi import APIRouter, HTTPException
from app.db.session import SessionLocal
from app.db.models import VectorRecord

router = APIRouter()

@router.put("/update/{record_id}")
def update_vector(record_id: int, text: str = None, embedding: list[float] = None):
	db = SessionLocal()
	try:
		record = db.query(VectorRecord).filter(VectorRecord.id == record_id).first()
		if not record:
			raise HTTPException(status_code=404, detail="Record not found")
		if text:
			record.text = text
		if embedding:
			record.embedding = embedding
		db.commit()
		return {"result": "updated"}
	except Exception as e:
		db.rollback()
		raise HTTPException(status_code=500, detail=str(e))
	finally:
		db.close()
