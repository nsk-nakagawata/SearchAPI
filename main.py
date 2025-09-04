from fastapi import FastAPI
from src.api import search, add, update, delete

app = FastAPI()

# ダミーエンドポイント
@app.get("/search")
def search_endpoint():
    return {"result": "search dummy response"}

@app.post("/add")
def add_endpoint():
    return {"result": "add dummy response"}

@app.put("/update")
def update_endpoint():
    return {"result": "update dummy response"}

@app.delete("/delete")
def delete_endpoint():
    return {"result": "delete dummy response"}
