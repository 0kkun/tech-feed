"""エントリーポイント: 収集 → フィルタ → 保存 → 通知"""
import logging

from src.collector import fetch_articles
from src.config import load_keywords
from src.db import get_today_articles, init_db, save_articles
from src.filter import filter_articles
from src.notifier import send_digest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Starting tech-feed")

    init_db()

    keywords = load_keywords()
    logger.info("Loaded %d keywords", len(keywords))

    raw_articles = fetch_articles()
    filtered = filter_articles(raw_articles, keywords)
    save_articles(filtered)

    today_articles = get_today_articles()
    send_digest(today_articles)

    logger.info("Finished tech-feed")


if __name__ == "__main__":
    main()
