from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn


app = FastAPI()

@app.get("/greeting/{name}")
def greet(name: str, formal: bool):
    if formal:
        return f"Dear {name}!"

    return f"Hello, {name}!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)