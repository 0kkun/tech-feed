# tech-feed

技術トレンドキャッチアップ用のニュース自動収集・メール通知システム。

## プロジェクト概要

- Zenn/QiitaからRSSで技術記事を日次収集
- キーワードフィルタリングしてPostgreSQLに保存
- 毎朝7時にSendGridで1日分のダイジェストメールを送信
- ローカルDocker環境で完結（デプロイなし）

## 技術スタック

- Python 3.12+（フレームワークなし）
- PostgreSQL
- SQLAlchemy（ORM）
- feedparser（RSS取得）
- SendGrid公式SDK（メール送信）
- cron（Docker内での定期実行）
- docker-compose

## ディレクトリ構成

最新の構成は `tree -a -I '.git|__pycache__' .` で確認すること。

基本構造:

```
tech-feed/
├── src/          # アプリケーションコード
├── tests/        # テスト
├── config/       # 設定ファイル（keywords.yml等）
├── cron/         # cron定義
├── .claude/      # Claude Code用ドキュメント・ルール
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env          # 環境変数（Git管理外）
└── .env.example  # 環境変数テンプレート
```

## 開発コマンド

```bash
# コンテナ起動
docker-compose up -d

# コンテナ停止
docker-compose down

# 手動実行（収集〜通知の一連処理）
docker-compose exec app python -m src.main

# テスト実行
docker-compose exec app python -m pytest tests/

# DB接続
docker-compose exec db psql -U techfeed -d techfeed
```

## 設計方針

- シンプルさを最優先。過度な抽象化はしない
- 設定値（キーワード、メールアドレス、SendGrid APIキー等）は環境変数または設定ファイルで管理
- .envファイルはGit管理外。.env.exampleをテンプレートとして管理
- キーワードはymlファイルで管理し、コード変更なしで追加・削除可能にする
- 重複排除はURLのユニーク制約 + `ON CONFLICT DO NOTHING`で実現

## 要件定義

詳細は `.claude/docs/requirements-20260618.md` を参照。
