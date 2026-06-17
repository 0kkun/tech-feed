# tech-feed

技術トレンドの記事を自動収集し、毎朝メールでダイジェスト配信するツール。

## 機能

- Zenn / Qiita から技術記事を日次収集（RSS）
- キーワードでフィルタリングして PostgreSQL に保存
- 毎朝7時に SendGrid で1日分をまとめてメール通知

## 技術スタック

Python / PostgreSQL / SQLAlchemy / SendGrid / Docker

## セットアップ

```bash
cp .env.example .env
# .env を編集（SendGrid APIキー、メールアドレス等）

docker-compose up -d
```

## 手動実行

```bash
docker-compose exec app python -m src.main
```
