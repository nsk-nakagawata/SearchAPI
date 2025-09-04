from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.db.models import Base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# テーブル作成（初回のみ）
Base.metadata.create_all(bind=engine)
