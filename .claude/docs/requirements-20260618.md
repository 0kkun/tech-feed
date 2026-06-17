# tech-feed 要件定義

## 概要

技術トレンドのキャッチアップを目的とした、ニュース自動収集・メール通知システム。
Zenn・Qiitaから技術記事を日次で収集し、キーワードでフィルタリングした上で、毎朝メールでダイジェスト配信する。

## 機能要件

### 1. 記事収集

- **情報ソース**
  - Zenn（RSS）
  - Qiita（RSS / API）
- **収集頻度:** 1日1回
- **取得データ:** タイトル、URL
- **フィルタリング:** タイトルに以下のキーワードを含む記事のみ保存

### 2. キーワード一覧

```
# AI/ML
AI, LLM, Claude, Anthropic, Gemini, OpenAI, RAG, 機械学習, 生成AI, Agent

# Cloud/Infra
AWS, Lambda, ECS, Fargate, Terraform, Docker, CDK

# Language/Framework
PHP, Laravel, Python

# DB
MySQL, PostgreSQL, Redis, DynamoDB

# Dev Practice
CI/CD, GitHub Actions, アーキテクチャ

# Security
セキュリティ, 脆弱性, OWASP

# Observability
OpenTelemetry, Datadog
```

※ キーワードは設定ファイル（env or config）で追加・削除可能にする

### 3. 重複排除

- URLをユニーク制約とし、同一記事の重複保存を防止する

### 4. メール通知

- **送信タイミング:** 毎朝7:00
- **形式:** 1日分の記事をまとめて1通で送信
- **送信先:** 自分のメールアドレス1件（設定ファイルで管理）
- **メール送信サービス:** SendGrid

## 非機能要件

### 技術スタック

| 項目 | 技術 |
|------|------|
| 言語 | Python（フレームワークなし） |
| DB | PostgreSQL |
| ORM | SQLAlchemy |
| RSS取得 | feedparser |
| メール送信 | SendGrid公式SDK |
| 定期実行 | cron（Docker内） |
| 実行環境 | ローカルDocker（docker-compose） |

### 構成イメージ

```
docker-compose.yml
├── app (Python)
│   ├── 記事収集スクリプト（cron実行）
│   └── メール送信スクリプト（cron実行）
└── db (PostgreSQL)
```

### 制約事項

- 画面（UI）は不要
- デプロイは行わない（ローカル完結）
- フレームワークは使用しない

## DB設計（概要）

### articles テーブル

| カラム | 型 | 備考 |
|--------|----|------|
| id | SERIAL / PK | |
| title | VARCHAR | 記事タイトル |
| url | VARCHAR / UNIQUE | 記事URL（重複排除キー） |
| source | VARCHAR | zenn / qiita |
| keyword | VARCHAR | マッチしたキーワード |
| created_at | TIMESTAMP | 取得日時 |

## 今後の拡張候補（スコープ外）

- 情報ソースの追加（はてなブックマーク、Hacker News、Dev.to、AWS公式ブログ、Laravel News等）
- 通知先の複数人対応
- Web UI（記事一覧・既読管理）
- 記事の要約生成（LLM活用）
