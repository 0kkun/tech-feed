.PHONY: up down build run test db logs

up: ## コンテナ起動
	docker compose up -d

down: ## コンテナ停止
	docker compose down

build: ## イメージ再ビルドして起動
	docker compose up -d --build

run: ## 手動実行（収集〜通知の一連処理）
	docker compose exec app python -m src.main

test: ## テスト実行
	docker compose exec app python -m pytest tests/

db: ## DB接続
	docker compose exec db psql -U techfeed -d techfeed

logs: ## ログ表示
	docker compose logs -f app

help: ## コマンド一覧表示
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | awk -F ':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'
