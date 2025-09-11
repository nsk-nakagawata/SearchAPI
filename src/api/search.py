
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
from src.db.session import SessionLocal
from src.db.models import AuditLog, Zairyom
from src.config.config import API_KEY
from src.utils.embedding import get_embedding
import logging

router = APIRouter()




# Dify外部ナレッジベースAPI仕様準拠の/retrievalエンドポイント
@router.post("/retrieval")
async def retrieval(request: Request):
	# 認証: Authorization: Bearer {API_KEY}
	auth_header = request.headers.get("Authorization")
	if not auth_header or not auth_header.startswith("Bearer "):
		return JSONResponse(status_code=401, content={"error_code": 1001, "error_msg": "無効な認証ヘッダー形式です。Bearer <api-key> 形式が期待されます。"})
	api_key = auth_header.replace("Bearer ", "").strip()
	if api_key != API_KEY:
		return JSONResponse(status_code=401, content={"error_code": 1002, "error_msg": "認証失敗"})

	try:
		body = await request.json()
	except Exception:
		return JSONResponse(status_code=400, content={"error_code": 400, "error_msg": "リクエストボディが不正です"})

	# 必須フィールドチェック
	for field in ["knowledge_id", "query", "retrieval_setting", "metadata_condition"]:
		if field not in body:
			return JSONResponse(status_code=400, content={"error_code": 400, "error_msg": f"{field}は必須です"})

	# 検索パラメータ取得
	query_text = body["query"]
	retrieval_setting = body["retrieval_setting"]
	top_k = retrieval_setting.get("top_k", 3)
	score_threshold = retrieval_setting.get("score_threshold", 0.5)
	# metadata_conditionは現状未対応（必要に応じて拡張）

	# query→embedding変換
	try:
		embedding = get_embedding(query_text)
	except Exception as e:
		logging.exception("embedding生成エラー")
		return JSONResponse(status_code=500, content={"error_code": 500, "error_msg": "embedding生成に失敗しました"})

	db = SessionLocal()
	try:
		# embeddingを使って近傍検索
		results = db.query(Zairyom).order_by(Zairyom.embedding.op('<->')(embedding)).limit(top_k*2).all()
		records = []
		for r in results:
			# 仮スコア: 1.0（本来はベクトル類似度）
			score = 1.0
			if score < score_threshold:
				continue
			records.append({
				"content": f"SYOCD={r.SYOCD}, HACNO={r.HACNO}, HACREN={r.HACREN}, UCHI={r.UCHI}, UCHI2={r.UCHI2}",
				"score": score,
				"title": f"{r.SYOCD}",
				"metadata": {}
			})
			if len(records) >= top_k:
				break
		# 監査ログ
		audit = AuditLog(
			user_id=None,
			operation="retrieval",
			request_data=str(body),
			response_data=str(records),
		)
		db.add(audit)
		db.commit()
		return {"records": records}
	except Exception as e:
		logging.exception("retrieval error")
		return JSONResponse(status_code=500, content={"error_code": 500, "error_msg": "内部サーバーエラー"})
	finally:
		db.close()


