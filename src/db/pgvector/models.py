from src.db.base import VectorDBBase
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class VectorModel(Base):
    __tablename__ = 'vectors'
    id = Column(Integer, primary_key=True)
    vector = Column(ARRAY(Float))
    metadata = Column(String)

class PgVectorDB(VectorDBBase):
    def add_vector(self, vector, metadata):
        # 実装例: SQLAlchemyで追加
        pass
    def update_vector(self, vector_id, vector, metadata):
        pass
    def delete_vector(self, vector_id):
        pass
    def search_vectors(self, query_vector, top_k=10):
        pass