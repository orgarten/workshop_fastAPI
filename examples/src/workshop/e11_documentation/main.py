from fastapi import FastAPI, status
import time
from typing import List
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Training",
    summary="A test API to show how to use docs in FastAPI",
    description="This API is for demonstration purposes for the FastAPI base_structure held online at GFU Cyrus AG. "
                "This can be a lot of text to provide context for this API and their documentation. \n\n "
                "Even more documentation to talk about the API.",
    version="1.0.0",
)


class ItemIn(BaseModel):
    name: str
    price: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "price": 250
                }
            ]
        }
    }


class ItemOut(BaseModel):
    id: int
    name: str
    price: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "iid": 1,
                    "name": "Foo",
                    "price": 250
                },
            ]
        }
    }

@app.get(
    "/items/",
    status_code=status.HTTP_200_OK,
    tags=["items"],
    response_model=List[ItemOut],
    summary="Return items from the catalog."
)
async def read_items():
    """
    `/items/` returns a list of items from the catalog. The item contains the information according to the `Item` schema.

    This is more information
    """
    return [{"id": 1, "name": "Foo", "price": 42}]

@app.put(
    "/items/",
    status_code=status.HTTP_200_OK,
    tags=["items"],
    response_model=ItemOut,
    summary="Add the item to the catalog if not present."
)
async def put_item(item: ItemIn):
    """
    `/items/` adds the item to the catalog if not present. If the item is already present in the catalog nothing changes.

    The response contains the newly created item including its ID.
    """
    return {"id": 1, **item.model_dump()}



