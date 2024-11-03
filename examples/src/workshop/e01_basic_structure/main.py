from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """This path operation is the most basic way to define an API route"""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """This path operation uses a path parameter to accept data"""
    return {"message": f"Hello {name}"}

@app.get("/hello")
async def say_hello(name: str):
    """This path operation can be used with a query parameter `name`."""
    return {"message": f"Hello {name}"}
