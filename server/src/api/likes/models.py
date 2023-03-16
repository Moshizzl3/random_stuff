from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    Table,
    DateTime,
    ForeignKey,
)
from ..users.models import Users
from ..posts.models import Posts

metaData = MetaData()

Likes = Table(
    "likes",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("created_on", DateTime),
    Column("user_id", Integer, ForeignKey(Users.c.id, ondelete="CASCADE")),
    Column("posts_id", Integer, ForeignKey(Posts.c.id, ondelete="CASCADE")),
)
