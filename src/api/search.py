from fastapi import APIRouter, Request
from typing import List
from src.auth.auth import api_key_auth
from src.api.response_models import SuccessResponse
from src.db.session import SessionLocal

from src.db.models import AuditLog, Zairyom


router = APIRouter()

from fastapi import Body

# ...existing code from app/api/search.py...

@router.post("/search", response_model=SuccessResponse)
async def search(
	request: Request,
	embedding: List[float] = Body(...)
):
	from fastapi import HTTPException

	api_key_auth(request)
	db = SessionLocal()
	# embedding配列の長さチェック
	dim = Zairyom.embedding.type.dim
	if len(embedding) != dim:
		raise HTTPException(status_code=400, detail=f"embeddingの次元数が不正です。要求: {dim}, 入力: {len(embedding)}")
	# embeddingベクトルによる近傍検索（pgvectorの<->演算子を利用/L2距離）
	try:
		query = db.query(Zairyom).order_by(Zairyom.embedding.op('<->')(embedding)).limit(5)
		results = query.all()
		response = SuccessResponse(data={
			"result": [f"SYOCD={r.SYOCD}, HACNO={r.HACNO}, HACREN={r.HACREN}" for r in results]
		})
		audit = AuditLog(
			user_id=None,
			operation="search",
			request_data=str(await request.body()),
			response_data=str(response),
		)
		db.add(audit)
		db.commit()
		return response
	finally:
		db.close()

# /search/retrieval エンドポイントを追加
@router.post("/search/retrieval", response_model=SuccessResponse)
async def search_retrieval(
	request: Request,
	embedding: List[float] = Body(...)
):
	return await search(request, embedding)
# ...existing code from app/api/search.py...
