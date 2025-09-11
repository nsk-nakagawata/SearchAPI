
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.db.models import Base
from src.config.config import get_database_url

DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# テーブル作成（初回のみ）
Base.metadata.create_all(bind=engine)
