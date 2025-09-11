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
# OpenAI APIキー（環境変数から取得、なければ空文字）
 # シークレット情報を削除しました
# ...existing code from app/config.py...
