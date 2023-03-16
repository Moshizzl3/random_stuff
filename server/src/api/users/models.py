from sqlalchemy import Column, Integer, MetaData, String, Table

metaData = MetaData()

Users = Table(
    "users",
    metaData,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(100)),
    Column("last_name", String(100)),
    Column("mail", String(50)),
    Column("profile_image_url", String(300)),
    Column("cover_image_url", String(300)),
    Column("password", String(500)),

)
