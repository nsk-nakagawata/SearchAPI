from fastapi import APIRouter, HTTPException
from app.db.session import SessionLocal
from app.db.models import VectorRecord

router = APIRouter()

@router.delete("/delete/{record_id}")
def delete_vector(record_id: int):
	db = SessionLocal()
	try:
		record = db.query(VectorRecord).filter(VectorRecord.id == record_id).first()
		if not record:
			raise HTTPException(status_code=404, detail="Record not found")
		db.delete(record)
		db.commit()
		return {"result": "deleted"}
	except Exception as e:
		db.rollback()
		raise HTTPException(status_code=500, detail=str(e))
	finally:
		db.close()
