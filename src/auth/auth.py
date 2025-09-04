from fastapi import Request, HTTPException
from src.config.config import API_KEY

def api_key_auth(request: Request):
	api_key = request.headers.get("X-API-Key")
	if api_key != API_KEY:
		raise HTTPException(status_code=401, detail="Invalid or missing API key")
# ...existing code from app/auth/auth.py...
