from typing import Annotated
from fastapi import FastAPI, status, Response, Depends


db = {}

def get_db() -> dict:
    return db

app = FastAPI()


@app.get("/hello/{name}", status_code=status.HTTP_200_OK)
async def hello(name: str, response: Response):
    if name != "alice":
        return {"message": f"Hello, {name}"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {}


@app.post("/name")
def post_name(
    name: str,
    age: int,
    fake_db: Annotated[dict, Depends(get_db)]
):
    fake_db.update({name: age})

    return fake_db

@app.get("/name/{name}")
def post_name(
    name: str,
    db: Annotated[dict, Depends(get_db)]
):
    age = db.get(name)
    return {name: age}

