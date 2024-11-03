import secrets

from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


@app.get("/")
async def main(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    # Warning: THIS IS NOT SECURE!!!
    return {"user": credentials.username, "password": credentials.password}


def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:

    username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"orell"

    valid_user = secrets.compare_digest(
        username_bytes, correct_username_bytes
    )

    # Warning: This is NOT production ready, but shows the concepts
    password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"swordfish"

    valid_password = secrets.compare_digest(
        password_bytes, correct_password_bytes
    )
    if not (valid_user and valid_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username

@app.get("/whoami")
async def get_current_user(username: Annotated[str, Depends(get_current_username)]):
    return {"username": username}