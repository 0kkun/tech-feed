---
description: Docker and infrastructure rules
paths: ['Dockerfile', 'docker-compose.yml', 'cron/**']
---

# Docker関連ルール

- ベースイメージは `python:3.12-slim` を使用する
- docker-compose.ymlでapp（Python）とdb（PostgreSQL）の2サービス構成
- cronはappコンテナ内で実行する
- ボリュームでDBデータを永続化する
- ヘルスチェックを設定し、DBが起動してからappが動くようにする
