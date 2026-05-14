from datetime import datetime
from typing import Optional

from sqlalchemy import Index, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .users import User, Base

class UserToken(Base):
    """
    用户令牌表ORM模型
    """
    __tablename__ = 'user_token'

    # 创建索引
    __table_args__ = (
        Index('token_UNIQUE', 'token'),
        Index('fk_user_token_user_idx', 'user_id'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="令牌ID")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(User.id), nullable=False, comment="用户ID")
    token: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, comment="令牌值")
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="过期时间")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), comment="创建时间")

    def __repr__(self):
        return f"<UserToken(id={self.id}, user_id={self.user_id}, token='{self.token}')>"