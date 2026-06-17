"""キーワードフィルタリング"""
import logging

logger = logging.getLogger(__name__)


def filter_articles(articles: list[dict], keywords: list[str]) -> list[dict]:
    """タイトルにキーワードを含む記事のみ返す。マッチしたキーワードを付与。"""
    filtered: list[dict] = []
    for article in articles:
        title = article["title"]
        for keyword in keywords:
            if keyword.lower() in title.lower():
                filtered.append({**article, "keyword": keyword})
                break
    logger.info("Filtered %d / %d articles", len(filtered), len(articles))
    return filtered
