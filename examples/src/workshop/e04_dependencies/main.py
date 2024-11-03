from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi import status, HTTPException

from pydantic import BaseModel


app = FastAPI()


def pagination_parameters(start: int, stop: int):
    if start > stop:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Start needs to be smaller than stop. Pagination is invalid"
        )

    return {"start": start, "stop": stop}

@app.get("/items")
def get_items(pagination: Annotated[dict, Depends(pagination_parameters)]):
    return {"pagination": pagination}


@app.get("/useres")
def get_users(pagination: Annotated[dict, Depends(pagination_parameters)]):
    return {"pagination": pagination}


class PaginationParams(BaseModel):
    start: int
    stop: int

def pagination_pydantic(start: int, stop: int):
    if start > stop:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Start needs to be smaller than stop. Pagination is invalid")

    return PaginationParams(start=start, stop=stop)




@app.get("/items_pydantic")
def get_items(pagination: Annotated[PaginationParams, Depends(pagination_pydantic)]):
    return {"pagination": pagination}
