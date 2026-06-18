"""Resendメール送信"""
import logging

import resend

from src.config import get_from_email, get_resend_api_key, get_to_email
from src.db import Article

logger = logging.getLogger(__name__)


def build_email_body(articles: list[Article]) -> str:
    """記事一覧からメール本文を生成する。"""
    lines = ["今日の技術記事ダイジェスト", "=" * 40, ""]
    for article in articles:
        lines.append(f"[{article.source}] {article.title}")
        lines.append(f"  {article.url}")
        lines.append(f"  keyword: {article.keyword}")
        lines.append("")
    lines.append(f"合計: {len(articles)} 件")
    return "\n".join(lines)


def send_digest(articles: list[Article]) -> None:
    """ダイジェストメールを送信する。"""
    if not articles:
        logger.info("No articles to send")
        return

    resend.api_key = get_resend_api_key()
    body = build_email_body(articles)

    params: resend.Emails.SendParams = {
        "from": get_from_email(),
        "to": [get_to_email()],
        "subject": f"tech-feed ダイジェスト ({len(articles)} 件)",
        "text": body,
    }

    response = resend.Emails.send(params)
    logger.info("Email sent: id=%s", response["id"])
