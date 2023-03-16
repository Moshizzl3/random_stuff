from fastapi import APIRouter, status, Depends
from .schemas import UserBase, UserInsert, UserSchema
from .models import Users
from typing import List
from ...database.db import database
from ..auth.token import get_current_user
from passlib.hash import pbkdf2_sha256


router = APIRouter(tags=["Users"])


@router.get("/users", response_model=List[UserBase])
async def get_users():
    query = Users.select()
    return await database.fetch_all(query)


@router.get("/api/users/name/", response_model=UserBase)
async def get_users_by_name(current_user: UserSchema = Depends(get_current_user)):
    query = Users.select().where(Users.c.id == current_user.id)
    user = await database.fetch_one(query)
    return user


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserInsert):
    hased_password = pbkdf2_sha256.hash(user.password)
    print(user)
    query = Users.insert().values(
        first_name=user.first_name,
        last_name=user.last_name,
        mail=user.mail,
        password=hased_password,
    )
    id = await database.execute(query)
    return {**user.dict(), "id": id}
