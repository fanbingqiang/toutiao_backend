"""SQLAlchemy ORM 模型"""
from datetime import datetime
from sqlalchemy import ForeignKey, Text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class NewsCategory(Base):
    """新闻分类"""
    __tablename__ = "news_categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    sort_order: Mapped[int] = mapped_column(default=0)
    create_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    news: Mapped[list["News"]] = relationship(back_populates="category")


class News(Base):
    """新闻"""
    __tablename__ = "news"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("news_categories.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(default="")
    cover_url: Mapped[str] = mapped_column(default="")
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(default="")
    author: Mapped[str] = mapped_column(default="")
    view_count: Mapped[int] = mapped_column(default=0)
    status: Mapped[int] = mapped_column(default=1)
    is_top: Mapped[int] = mapped_column(default=0)
    publish_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    create_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    category: Mapped["NewsCategory"] = relationship(back_populates="news")


class User(Base):
    """用户"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    nickname: Mapped[str] = mapped_column(default="")
    avatar: Mapped[str] = mapped_column(default="")
    role: Mapped[int] = mapped_column(default=0)
    status: Mapped[int] = mapped_column(default=1)
    create_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class AiChat(Base):
    """AI聊天记录"""
    __tablename__ = "aichat"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    role: Mapped[str] = mapped_column(default="user")
    content: Mapped[str] = mapped_column(Text, nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class Favorite(Base):
    """新闻收藏"""
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    news_id: Mapped[int] = mapped_column(ForeignKey("news.id"), nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class ReloadHistory(Base):
    """新闻刷新历史"""
    __tablename__ = "reload_history"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("news_categories.id"), nullable=True)
    source: Mapped[str] = mapped_column(default="")
    news_count: Mapped[int] = mapped_column(default=0)
    status: Mapped[int] = mapped_column(default=1)
    message: Mapped[str] = mapped_column(default="")
    create_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class Category:
    pass