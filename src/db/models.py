from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()


class AuditLog(Base):
	__tablename__ = "audit_logs"
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(String(128), nullable=True)
	operation = Column(String(64), nullable=False)
	request_data = Column(Text, nullable=True)
	response_data = Column(Text, nullable=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# zairyomテーブルのモデル定義
from sqlalchemy.dialects.postgresql import VECTOR

class Zairyom(Base):
	__tablename__ = 'zairyom'
	SYOCD = Column(String, primary_key=True)
	HACNO = Column(String, primary_key=True)
	HACREN = Column(String, primary_key=True)
	embedding = Column(VECTOR(1536))  # 1536次元を例示。必要に応じて次元数を変更
	# 必要に応じて他カラムを追加
	# name = Column(String)
	# description = Column(String)
