from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class VectorRecord(Base):
	__tablename__ = "vector_records"
	id = Column(Integer, primary_key=True, index=True)
	text = Column(String, nullable=False)
	embedding = Column(Vector(1536))  # 例: OpenAI embeddingサイズ
