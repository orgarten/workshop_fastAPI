from fastapi import FastAPI
from fastapi import status, Response
from ..e05_middleware import logging_middleware

app = FastAPI()
app.add_middleware(logging_middleware.LoggingMiddleware)

@app.get("/hello", status_code=status.HTTP_200_OK)
async def hello():
    return {"message": "Hello World!"}

