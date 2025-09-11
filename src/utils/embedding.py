import os
import requests
from typing import List

from src.config.config import OPENAI_API_KEY

OPENAI_EMBEDDING_ENDPOINT = "https://api.openai.com/v1/embeddings"
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"


def get_embedding(text: str) -> List[float]:
    """
    OpenAI APIを使ってテキストからembeddingを生成する
    """
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "input": text,
        "model": OPENAI_EMBEDDING_MODEL
    }
    response = requests.post(OPENAI_EMBEDDING_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()
    embedding = response.json()["data"][0]["embedding"]
    return embedding
