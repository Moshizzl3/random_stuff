from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    mail: str
    profile_image_url: Optional[str] = None
    cover_image_url: Optional[str] = None


class UserInsert(BaseModel):
    first_name: str
    last_name: str
    mail: str
    password: str


class UserSchema(BaseModel):
    id: str
