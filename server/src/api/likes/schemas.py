from pydantic import BaseModel
from datetime import datetime


class LikeInsert(BaseModel):
    created_on: datetime
    user_id: int
    posts_id: int


class LikeBase(LikeInsert):
    id: int
