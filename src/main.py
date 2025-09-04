from fastapi import FastAPI, HTTPException
from src.api.search import router as search_router
from src.api.add import router as add_router
from src.api.update import router as update_router
from src.api.delete import router as delete_router
from src.api.error_handlers import http_exception_handler, generic_exception_handler

app = FastAPI()

app.include_router(search_router)
app.include_router(add_router)
app.include_router(update_router)
app.include_router(delete_router)

# 例外ハンドラ登録
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
