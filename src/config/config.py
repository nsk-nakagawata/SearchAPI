# データベース接続情報
DB_CONFIG = {
	'dbname': 'postgres',
	'user': 'postgres',
	'password': 'NskAdmin5072',
	'host': 'localhost',
	'port': 5432
}

def get_database_url():
	cfg = DB_CONFIG
	return f"postgresql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['dbname']}"
# APIキー設定
import os
API_KEY = os.getenv("API_KEY", "api-key-1234567890")

# OpenAI APIキー（環境変数から取得、なければ空文字）
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "***REMOVED***proj-zJuBwYE36OXeid2vtnnJsrj6att5UomjRLPlk1m03d6BxaIU_euZccAVDwEsoajQ2xqMbY7HtNT3BlbkFJDAVKHv7jNA6l2zNhGFz2MrZZkkgIaPlwz3kvPEcta6TGAQGTaln9TWKsohKTz1x9TgoJmm82AA")
# ...existing code from app/config.py...
