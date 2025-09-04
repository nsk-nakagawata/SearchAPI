from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.search import router as search_router
from src.api.add import router as add_router
from src.api.update import router as update_router
from src.api.delete import router as delete_router
from src.api.error_handlers import http_exception_handler, generic_exception_handler

from src.utils.logging_middleware import LoggingMiddleware


app = FastAPI()
app.add_middleware(LoggingMiddleware)

# CORS設定（全許可）
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(search_router)
app.include_router(add_router)
app.include_router(update_router)
app.include_router(delete_router)

# 例外ハンドラ登録
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
