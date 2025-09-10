# Difyナレッジベース × 外部ベクトルDB連携API アーキテクチャ案

## 概要
Difyのナレッジベース機能と、PostgreSQLベクトルDB（pgvector等）を外部API経由で連携するためのアーキテクチャ案です。

---

## 構成

- **Difyアプリケーション**
  - ナレッジベース機能を持つDify本体。
  - 外部API経由でベクトル検索を実行。

- **APIサーバー（本プロジェクト）**
  - Difyからのリクエストを受け、PostgreSQLベクトルDBに対してREST APIで検索・登録・更新などを行う。
  - Python（FastAPI/Flask等）で実装。

- **PostgreSQL（ベクトルDB拡張付き）**
  - テーブル「zairyom」のカラム「embedding」にベクトルを格納。
  - pgvector等の拡張を利用し、embeddingカラムでベクトル検索をサポート。

---

## APIサーバー設計

- **主なエンドポイント例**
  - `/search`：ベクトル検索（クエリベクトルを受け取り、類似データを返す）
  - `/add`：ベクトルデータの追加
  - `/update`：ベクトルデータの更新
  - `/delete`：ベクトルデータの削除

- **認証・認可**
  - APIキーやJWT等で認証

- **DB接続**
  - SQLAlchemyやpsycopg2でPostgreSQLに接続
  - ベクトル検索はpgvectorの`<->`演算子等を利用

---

## データフロー

1. DifyがAPIサーバーの`/search`等のエンドポイントにリクエスト
2. APIサーバーがクエリベクトルを受け取り、PostgreSQLのzairyomテーブルのembeddingカラムに対してベクトル検索SQLを発行
3. 検索結果をAPIサーバーが整形し、Difyに返却

---

## セキュリティ・運用

- APIサーバーはDocker化推奨
- PostgreSQLは外部公開せず、APIサーバーのみがアクセス
- ログ・監査機能の実装

---

## 拡張性

- ベクトルDBの種類変更（Milvus等）にも対応しやすい設計
- Dify以外のクライアントからも利用可能な汎用API

---

## 次のステップ

1. FastAPIでAPIサーバーの雛形を作成
2. PostgreSQL（pgvector）との接続・ベクトル検索の実装
3. Difyとの連携テスト

---

ご要望に応じて、APIサーバーの雛形コードやDBスキーマ例も作成可能です。
