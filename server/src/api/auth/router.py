from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ...database.db import database
from ..users.models import Users
from passlib.hash import pbkdf2_sha256
from .token import create_access_token


router = APIRouter(tags=["Auth"])


@router.post("/api/authenticate/")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    print(request)
    print("hello")
    query = Users.select().where(Users.c.mail == request.username)
    myuser = await database.fetch_one(query)
    if not myuser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not pbkdf2_sha256.verify(request.password, myuser.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="wrong password"
        )

    access_token = create_access_token(data={"mail": myuser.mail, "id": myuser.id})
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}
