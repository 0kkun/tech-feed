"""RSS取得・パース"""
import logging

import feedparser

logger = logging.getLogger(__name__)

FEED_URLS: dict[str, str] = {
    "zenn": "https://zenn.dev/feed",
    "qiita": "https://qiita.com/popular-items/feed",
}


def fetch_articles() -> list[dict]:
    """全フィードから記事を取得してリストで返す。"""
    articles: list[dict] = []
    for source, url in FEED_URLS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                articles.append({
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "source": source,
                })
            logger.info("Fetched %d articles from %s", len(feed.entries), source)
        except Exception:
            logger.exception("Failed to fetch from %s", source)
    return articles
