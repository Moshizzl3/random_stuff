from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.users.router import router as users_router
from .api.posts.router import router as posts_router
from .api.likes.router import router as likes_router
from .api.files.router import router as files_router
from .api.auth.router import router as auth_router
from .database.db import database, engine, metaData

metaData.create_all(engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users_router)
app.include_router(posts_router)
app.include_router(likes_router)
app.include_router(auth_router)
app.include_router(files_router)
