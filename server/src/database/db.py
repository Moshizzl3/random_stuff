from sqlalchemy import create_engine, MetaData
from databases import Database
from ..api.users.models import Users
from ..api.posts.models import Posts
from ..api.likes.models import Likes
from passlib.hash import pbkdf2_sha256

DATABASE_URL = "mysql+pymysql://myuser:mypassword@db/mydb"

metaData = MetaData()
engine = create_engine(DATABASE_URL)


database = Database(DATABASE_URL)

# Test data

try:
    Likes.drop(engine)
    Posts.drop(engine)
    Users.drop(engine)
    Users.create(engine)
    Posts.create(engine)
    Likes.create(engine)
except Exception as e:
    Users.create(engine)
    Posts.create(engine)
    Likes.create(engine)


my_user1 = [
    None,
    "Mo",
    "Ib",
    "mail@mail.dk",
    "mo.jpeg",
    "space.jpg",
    pbkdf2_sha256.hash("hello"),
]

my_user2 = [
    None,
    "fin",
    "jensen",
    "mail1@mail.dk",
    "fin.jpg",
    "mountain.jpg",
    pbkdf2_sha256.hash("1234"),
]

engine.execute(Users.insert().values(my_user1))
engine.execute(Users.insert().values(my_user2))


# Posts

my_post1 = [
    None,
    "This is a post",
    "22-10-10",
    "some-img",
    1,
]
my_post2 = [
    None,
    "This is a post",
    "22-10-10",
    "some-img",
    2,
]

engine.execute(Posts.insert().values(my_post1))
engine.execute(Posts.insert().values(my_post1))
engine.execute(Posts.insert().values(my_post2))
engine.execute(Posts.insert().values(my_post2))

# Likes

my_like1 = [
    None,
    "22-10-10",
    1,
    1,
]

engine.execute(Likes.insert().values(my_like1))
engine.execute(Likes.insert().values(my_like1))
