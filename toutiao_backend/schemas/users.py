from pydantic import BaseModel, Field, ConfigDict


class UserRequest(BaseModel):
    username: str
    password: str

class UserInfoResponse(BaseModel):
    username: str
    password: str

class UserAUTHRespone(BaseModel):
    token: str
    user_info: UserInfoResponse = Field(...,alias="userInfo")

    model_config = ConfigDict(
        
    )