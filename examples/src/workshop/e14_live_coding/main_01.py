from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add_query(n1: int, n2: int):
    """ Query Parameter"""
    return {"result": n1 + n2}


@app.get("/add/{n1}/{n2}")
def add_path(n1: int, n2: int):
    """ Path Parameter"""
    return {"result": n1 + n2}
