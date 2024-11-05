import secrets

from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

user_db = {
    "orell": {
        "password": "swordfish",
        "is_admin": False
    },
    "admin": {
        "password": "adminpassword",
        "is_admin": True
    }
}

@app.get("/")
async def main(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    # Warning: THIS IS NOT SECURE!!!
    return {"user": credentials.username, "password": credentials.password}


def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:

    if credentials.username not in user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    # Warning: This is NOT production ready, but shows the concepts
    password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = user_db[credentials.username]["password"].encode("utf8")

    valid_password = secrets.compare_digest(
        password_bytes, correct_password_bytes
    )
    if not valid_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username

@app.get("/whoami")
async def get_current_user(username: Annotated[str, Depends(get_current_username)]):
    return {"username": username}


def check_admin(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> bool:

    if credentials.username not in user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    if not user_db[credentials.username]["is_admin"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return True


@app.get("/admin", dependencies=[Depends(check_admin)])
async def get_admin(username: Annotated[str, Depends(get_current_username)]):
    return {"message": f"admin access granted for {username}"}