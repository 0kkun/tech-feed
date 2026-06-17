---
description: Python coding standards for this project
paths: ['src/**/*.py', 'tests/**/*.py']
---

# コーディング規約

- Python 3.12+ の機能を使用してよい
- 型ヒントを必ず付ける（関数の引数・戻り値）
- フォーマッターは使わない（シンプルにPEP 8準拠）
- クラスは必要最小限。関数ベースで書く
- 1ファイルの責務は1つに絞る
- ログ出力には標準ライブラリの `logging` を使用する（printは使わない）
- 外部APIの呼び出しにはリトライ処理を入れる
