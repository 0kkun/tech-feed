"""Resendメール送信"""
import logging

import resend

from src.config import get_from_email, get_resend_api_key, get_to_email
from src.db import Article

logger = logging.getLogger(__name__)


def build_email_html(articles: list[Article]) -> str:
    """記事一覧からHTMLメール本文を生成する。"""
    # ソース別にグルーピング
    grouped: dict[str, list[Article]] = {}
    for article in articles:
        grouped.setdefault(article.source, []).append(article)

    source_labels = {"zenn": "Zenn", "qiita": "Qiita"}
    sections = ""
    for source, items in grouped.items():
        label = source_labels.get(source, source)
        rows = ""
        for a in items:
            rows += f"""\
            <tr>
              <td style="padding: 8px 12px; border-bottom: 1px solid #eee;">
                <a href="{a.url}" style="color: #1a73e8; text-decoration: none; font-size: 14px;">{a.title}</a>
                <br><span style="color: #888; font-size: 12px;">#{a.keyword}</span>
              </td>
            </tr>"""
        sections += f"""\
        <tr>
          <td style="padding: 16px 12px 4px; font-size: 15px; font-weight: bold; color: #333;">{label}（{len(items)}件）</td>
        </tr>
        {rows}"""

    return f"""\
<html>
<body style="margin: 0; padding: 0; background: #f5f5f5; font-family: -apple-system, sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 24px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background: #fff; border-radius: 8px; overflow: hidden;">
          <tr>
            <td style="padding: 20px 24px; background: #1a73e8; color: #fff; font-size: 18px; font-weight: bold;">
              tech-feed ダイジェスト
            </td>
          </tr>
          {sections}
          <tr>
            <td style="padding: 16px 12px; text-align: right; color: #888; font-size: 13px; border-top: 2px solid #eee;">
              合計 {len(articles)} 件
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""


def send_digest(articles: list[Article]) -> None:
    """ダイジェストメールを送信する。"""
    if not articles:
        logger.info("No articles to send")
        return

    resend.api_key = get_resend_api_key()
    html = build_email_html(articles)

    params: resend.Emails.SendParams = {
        "from": get_from_email(),
        "to": [get_to_email()],
        "subject": f"tech-feed ダイジェスト ({len(articles)} 件)",
        "html": html,
    }

    response = resend.Emails.send(params)
    logger.info("Email sent: id=%s", response["id"])
