from fastapi import FastAPI
from fastapi import status, Response


app = FastAPI()


@app.get("/hello/{name}", status_code=status.HTTP_200_OK)
async def hello(name: str, response: Response):
    if name != "alice" and name != "bob":
        return {"message", f"Hello, {name}"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    # ↑ vs ↓
    raise exceptions.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Name not allowed"
    )

    return {"message": "Name not allowed"}


from fastapi import exceptions

@app.get("/hello_with_exception/{name}", status_code=status.HTTP_200_OK)
async def hello2(name: str):
    if name == "alice" or name == "bob":
        raise exceptions.HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Name not allowed"
        )

    return {"message": f"Hello, {name}"}








