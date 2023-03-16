from fastapi import APIRouter
from .schemas import LikeBase
from .models import Likes
from typing import List
from ...database.db import database


router = APIRouter(tags=["Likes"])


@router.get("/likes", response_model=List[LikeBase])
async def get_likes():
    query = Likes.select()
    likes = await database.fetch_all(query)
    return likes
