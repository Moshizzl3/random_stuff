from pydantic import BaseModel


class TokenData(BaseModel):
    mail: str
    id: int
