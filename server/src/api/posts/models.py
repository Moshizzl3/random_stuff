from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    DateTime,
    ForeignKey,
)
from ..users.models import Users

metaData = MetaData()

Posts = Table(
    "posts",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("text", String(300)),
    Column("created_on", DateTime),
    Column("image_url", String(50)),
    Column("user_id", Integer, ForeignKey(Users.c.id, ondelete="CASCADE")),
)
