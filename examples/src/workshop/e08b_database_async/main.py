from fastapi import FastAPI, Form, Depends
from typing import Annotated
from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from contextlib import asynccontextmanager

class CustomBase(AsyncAttrs, DeclarativeBase):
    pass

class User(CustomBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    email: Mapped[str] = mapped_column(String(1024))


engine = create_async_engine("sqlite+aiosqlite:///example.db")
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with session_maker() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(CustomBase.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)

@app.post("/user")
async def add_user(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    db: Annotated[AsyncSession, Depends(get_session)]
):
    user = User(name=name, email=email)

    db.add(user)
    await db.commit()

    return {"id": user.id, "name": user.name, "email": user.email}


@app.get("/user")
async def get_user(
    db: Annotated[AsyncSession, Depends(get_session)]
):

    stmt = select(User)
    result = await db.scalars(stmt)

    return [{"id": user.id, "name": user.name, "email": user.email} for user in result.all()]


@app.get("/user/{id}")
async def get_user(
    id: int,
    db: Annotated[AsyncSession, Depends(get_session)]
):

    stmt = select(User).where(User.id == id)
    user = await db.scalars(stmt)
    user = user.one()

    return {"id": user.id, "name": user.name, "email": user.email}

