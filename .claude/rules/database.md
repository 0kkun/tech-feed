---
description: Database design and operation rules
paths: ['src/db.py', 'src/main.py']
---

# データベースルール

- ORMはSQLAlchemyを使用する
- テーブル定義は `src/db.py` にモデルとして記述する
- マイグレーションツールは使わない（初回起動時に `create_all` で作成）
- 重複排除は `url` カラムのUNIQUE制約 + `ON CONFLICT DO NOTHING` で実現する
- タイムゾーンは Asia/Tokyo を使用する
