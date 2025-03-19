from fastapi import FastAPI, status
import time
from typing import List
from pydantic import BaseModel

app = FastAPI()


@app.get("/test1")
async def test1():
    time.sleep(15)
    return {"message": "Hello World from /test1"}


@app.get("/test1_check")
def test1_check():
    return {"message": "Hello World from /test1_check"}


@app.get("/test2")
def test2():
    time.sleep(15)
    return {"message": "Hello World from /test2"}


@app.get("/test2_check")
async def test2_check():
    return {"message": "Hello World from /test2_check"}


