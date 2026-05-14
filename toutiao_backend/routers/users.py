from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse

from crud import users
from schemas.users import UserRequest

from config.db_conf import get_db

router = APIRouter(prefix="/api/user", tags=["users"])

@router.post("/register")
async def register(user_data: UserRequest,db:AsyncSession=Depends(get_db),):
    #REGISER exit? create token return
    exiting_user = users.get_user_by_username(db, user_data.username)
    if exiting_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user = await users.create_user(db, user_data)
    #token
    token = await users.create_token(db, user.id)

    # return {
    #     "code": 200,
    #     "message": "user registered",
    #     "data": {
    #         "token": token,
    #         "userInfo":{
    #             "id": user.id,
    #             "username": user.username,
    #             "bio": user.bio,
    #             "avatar": user.avatar,
    #         }
    #     }
    # }