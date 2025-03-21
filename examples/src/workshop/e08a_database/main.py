from fastapi import FastAPI, Form, Depends
from typing import Annotated
from sqlalchemy import create_engine,  String, select, delete
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session


class CustomBase(DeclarativeBase):
    pass

class User(CustomBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    email: Mapped[str] = mapped_column(String(1024))


engine = create_engine("sqlite:///example.db")
session_maker = sessionmaker(bind=engine)
CustomBase.metadata.create_all(engine)


def get_session() -> Session:
    with session_maker() as session:
        yield

app = FastAPI()


@app.post("/user")
def add_user(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    db: Annotated[Session, Depends(get_session)]
):
    user = User(name=name, email=email)

    db.add(user)
    db.commit()

    return {"id": user.id, "name": user.name, "email": user.email}


@app.get("/user")
def get_user(
        db: Annotated[Session, Depends(get_session)]
):

    stmt = select(User)
    result = db.scalars(stmt).all()

    return [{"id": user.id, "name": user.name, "email": user.email} for user in result]


@app.get("/user/{id}")
def get_user(
        id: int,
        db: Annotated[Session, Depends(get_session)]
):

    stmt = select(User).where(User.id == id)
    user = db.scalars(stmt).one()

    return {"id": user.id, "name": user.name, "email": user.email}

@app.delete("/user/{id}")
def delete_user(id: int, db: Annotated[Session, Depends(get_session)]):
    stmt = delete(User).where(User.id == id)

    db.execute(stmt)
    db.commit()

    return {"message": "User deleted"}

