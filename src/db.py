"""DB接続・モデル定義・CRUD"""
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.config import get_database_url

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    source = Column(String, nullable=False)
    keyword = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")))


def get_engine():
    return create_engine(get_database_url())


def get_session() -> Session:
    engine = get_engine()
    return sessionmaker(bind=engine)()


def init_db() -> None:
    """テーブルを作成する。"""
    engine = get_engine()
    Base.metadata.create_all(engine)
    logger.info("Database initialized")


def save_articles(articles: list[dict]) -> int:
    """記事を保存する。重複はスキップ。保存件数を返す。"""
    if not articles:
        return 0
    engine = get_engine()
    saved = 0
    with Session(engine) as session:
        for article in articles:
            stmt = insert(Article).values(
                title=article["title"],
                url=article["url"],
                source=article["source"],
                keyword=article["keyword"],
            ).on_conflict_do_nothing(index_elements=["url"])
            result = session.execute(stmt)
            if result.rowcount > 0:
                saved += 1
        session.commit()
    logger.info("Saved %d / %d articles", saved, len(articles))
    return saved


def get_today_articles() -> list[Article]:
    """今日保存された記事を取得する。"""
    engine = get_engine()
    with Session(engine) as session:
        today = datetime.now(ZoneInfo("Asia/Tokyo")).replace(hour=0, minute=0, second=0, microsecond=0)
        return session.query(Article).filter(Article.created_at >= today).all()
