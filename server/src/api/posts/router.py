from fastapi import APIRouter, Depends
from .schemas import PostBase
from .models import Posts
from ..users.schemas import UserSchema
from typing import List
from ...database.db import database
from ..auth.token import get_current_user


router = APIRouter(tags=["Posts"])


@router.get("/api/posts", response_model=List[PostBase])
async def get_posts(current_user: UserSchema = Depends(get_current_user)):
    query = Posts.select()
    posts = await database.fetch_all(query)
    return posts
