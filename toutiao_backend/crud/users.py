import datetime
import uuid
from idlelib import query

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.news import User
from models.usertoken import UserToken
from schemas.users import UserRequest
from utils import security


async def get_user_by_username(db:AsyncSession,username: str):
    query = select(User).where(User.username == username)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def create_user(db:AsyncSession,user_data: UserRequest,):
    #加密 add
    security.get_password_hash(user_data.password)
    user = User(username=user_data.username,password=hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

#生成token
async def create_token(db:AsyncSession,user_id: int):
    token = str(uuid.uuid4())
    expires_at = datetime.utcnow() + datetime.timedelta(minutes=10)
    query = select(UserToken).where(UserToken.user_id == user_id)
    result = await db.execute(query)
    user_token = result.scalar_one_or_none()

    if not user_token:
        user_token = UserToken(user_id=user_id,token=token,expires_at=expires_at)
        db.add(user_token)
        await db.commit()
    else:
        user_token.token = token
        user_token.expires_at = expires_at

    return token