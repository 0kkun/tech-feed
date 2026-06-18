"""設定読み込み"""
import os
from pathlib import Path

import yaml


def load_keywords(config_path: str | None = None) -> list[str]:
    """keywords.ymlからキーワード一覧をフラットなリストで返す。"""
    if config_path is None:
        config_path = str(Path(__file__).parent.parent / "config" / "keywords.yml")
    with open(config_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    keywords: list[str] = []
    for category_keywords in data.values():
        keywords.extend(category_keywords)
    return keywords


def get_database_url() -> str:
    return os.environ["DATABASE_URL"]


def get_resend_api_key() -> str:
    return os.environ["RESEND_API_KEY"]


def get_from_email() -> str:
    return os.environ["FROM_EMAIL"]


def get_to_email() -> str:
    return os.environ["TO_EMAIL"]
