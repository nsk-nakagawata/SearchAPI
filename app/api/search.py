from fastapi import APIRouter, HTTPException
from app.db.session import SessionLocal
from app.db.models import VectorRecord
from sqlalchemy import text

router = APIRouter()

@router.post("/search")
def search_vector(embedding: list[float], top_k: int = 5):
	db = SessionLocal()
	try:
		# pgvectorの<->演算子を用いた類似検索
		sql = text("""
			SELECT id, text, embedding
			FROM vector_records
			ORDER BY embedding <-> :embedding
			LIMIT :top_k
		""")
		results = db.execute(sql, {"embedding": embedding, "top_k": top_k}).fetchall()
		return [{"id": r[0], "text": r[1]} for r in results]
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
	finally:
		db.close()
