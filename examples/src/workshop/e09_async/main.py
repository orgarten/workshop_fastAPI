from fastapi import FastAPI, status
import time
from typing import List
from pydantic import BaseModel

app = FastAPI()


@app.get("/test1")
async def test():
    time.sleep(15)
    return {"message": "Hello World from /test1"}


@app.get("/test1_check")
def test_no_async():
    return {"message": "Hello World from /test1_check"}


@app.get("/test2")
def test_no_async():
    time.sleep(15)
    return {"message": "Hello World from /test2"}


@app.get("/test2_check")
async def test():
    return {"message": "Hello World from /test2_check"}


