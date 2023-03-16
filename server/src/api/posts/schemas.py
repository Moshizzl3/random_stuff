from pydantic import BaseModel
from datetime import datetime


class PostInsert(BaseModel):
    text: str
    created_on: datetime
    image_url: str
    user_id: int


class PostBase(PostInsert):
    id: int
