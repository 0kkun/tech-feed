---
description: Rules for handling configuration and secrets
paths: ['**/*.py', '**/*.yml', 'docker-compose.yml', '.env.example']
---

# 設定・機密情報の取り扱い

- APIキー・メールアドレス等の機密情報は `.env` で管理し、コードにハードコードしない
- `.env` はGit管理外。`.env.example` に変数名のみ記載する
- キーワード一覧は `config/keywords.yml` で管理する
- 設定の読み込みは `src/config.py` に集約する
- 新しい環境変数を追加したら `.env.example` も必ず更新する
