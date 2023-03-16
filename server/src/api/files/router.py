from fastapi import APIRouter, Depends, status
from fastapi.responses import FileResponse
from ...database.db import database
from ..users.schemas import UserSchema
from ..users.models import Users
from ..auth.token import get_current_user

router = APIRouter()


@router.get("/api/images/profile-image")
async def get_profile_image(current_user: UserSchema = Depends(get_current_user)):
    query = Users.select().where(current_user.id == Users.c.id)
    user = await database.fetch_one(query)
    userurl = user.profile_image_url
    return FileResponse("src/public/images/" + userurl)


# @router.get("/api/images/img-name/{img_name}")
# async def get_image_by_name(
#     img_name: str, current_user: UserSchema = Depends(get_current_user)
# ):
#     return FileResponse("src/public/images/" + img_name)


@router.get("/profile-image/follower/{id}")
async def get_follower_profile_image(
    current_user: UserSchema = Depends(get_current_user),
):
    return FileResponse("src/public/images/morph.jpeg")
