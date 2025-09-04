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
