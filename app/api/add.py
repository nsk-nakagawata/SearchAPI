from fastapi import APIRouter, HTTPException
from app.db.session import SessionLocal
from app.db.models import VectorRecord, Base

router = APIRouter()

@router.post("/add")
def add_vector(text: str, embedding: list[float]):
	db = SessionLocal()
	try:
		record = VectorRecord(text=text, embedding=embedding)
		db.add(record)
		db.commit()
		db.refresh(record)
		return {"id": record.id}
	except Exception as e:
		db.rollback()
		raise HTTPException(status_code=500, detail=str(e))
	finally:
		db.close()
