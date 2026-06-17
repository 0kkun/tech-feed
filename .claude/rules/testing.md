---
description: Testing rules
paths: ['tests/**/*.py']
---

# テストルール

- テストフレームワークは pytest を使用する
- テストファイル名は `test_` プレフィックスを付ける
- 外部API（RSS取得・SendGrid）のテストではモックを使用する
- DBのテストではテスト用のDBまたはSQLiteを使用する
